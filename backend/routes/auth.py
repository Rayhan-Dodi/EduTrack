from fastapi import APIRouter, Depends, HTTPException, Request, Response, Form
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models as _models
from ..schemas.schemas import UserCreate, UserOut
from ..utils.auth import hash_password, verify_password
from ..utils import jwt as jwt_utils
from datetime import timedelta

router = APIRouter()

@router.post('/register', response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(_models.models.User).filter_by(username=user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail='Username already exists')
    user = _models.models.User(
        username=user_in.username,
        hashed_password=hash_password(user_in.password),
        full_name=user_in.full_name,
        role=user_in.role
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post('/login')
def login(response: Response, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(_models.models.User).filter_by(username=username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = jwt_utils.create_access_token({'sub': user.username, 'role': user.role}, expires_delta=timedelta(minutes=60*24))
    # return token in JSON (frontend JS will store it)
    return {'access_token': token, 'token_type': 'bearer'}

def get_current_user(token: str = Depends(lambda: None), db: Session = Depends(get_db)):
    # This function will be overridden by dependency in students routes using OAuth2 header.
    raise HTTPException(status_code=401, detail='Not implemented')
