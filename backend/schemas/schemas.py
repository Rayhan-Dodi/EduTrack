from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import datetime

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)
    full_name: Optional[str]
    role: Optional[str] = 'teacher'

class UserOut(BaseModel):
    id: int
    username: str
    full_name: Optional[str]
    role: str
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    student_id: str
    first_name: str
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str] = None
    blood_group: Optional[str] = None
    birthdate: Optional[datetime.date] = None
    address: Optional[str] = None
    notes: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    created_at: Optional[datetime.datetime]
    class Config:
        orm_mode = True
