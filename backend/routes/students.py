from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models as _models
from ..schemas.schemas import StudentCreate, StudentOut
from .deps import get_current_user

router = APIRouter()

@router.post('/', response_model=StudentOut)
def create_student(student_in: StudentCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    existing = db.query(_models.models.Student).filter_by(student_id=student_in.student_id).first()
    if existing:
        raise HTTPException(status_code=400, detail='Student ID already exists')
    student = _models.models.Student(**student_in.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@router.get('/', response_model=List[StudentOut])
def list_students(skip: int = 0, limit: int = 50, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    students = db.query(_models.models.Student).offset(skip).limit(limit).all()
    return students

@router.get('/{student_id}', response_model=StudentOut)
def get_student(student_id: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    student = db.query(_models.models.Student).filter_by(student_id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student
