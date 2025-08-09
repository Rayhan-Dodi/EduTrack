from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory='web/templates')

@router.get('/', response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

@router.get('/students', response_class=HTMLResponse)
def students_page(request: Request):
    return templates.TemplateResponse('students.html', {'request': request})
