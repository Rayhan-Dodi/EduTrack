from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models as _models
from ..utils import jwt as jwt_utils

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt_utils.verify_token(token)
        username = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Invalid authentication')
    except Exception:
        raise HTTPException(status_code=401, detail='Invalid authentication')
    user = db.query(_models.models.User).filter_by(username=username).first()
    if not user:
        raise HTTPException(status_code=401, detail='User not found')
    return user
