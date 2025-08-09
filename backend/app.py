from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import auth, students
from ..web import views as web_views

Base.metadata.create_all(bind=engine)

app = FastAPI(title='EduTrack API', version='0.1.0')

app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(web_views.router, tags=['web'])
app.include_router(students.router, prefix='/students', tags=['students'])

@app.get('/')
async def root():
    return {'message': 'Welcome to EduTrack API'}
