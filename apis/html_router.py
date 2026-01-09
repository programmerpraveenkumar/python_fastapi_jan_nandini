from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home", response_class=HTMLResponse)
def home():
    return templates.TemplateResponse("home.html" )

@router.get("/question", response_class=HTMLResponse)
def question():
   return templates.TemplateResponse("question.html" )

@router.get("/final", response_class=HTMLResponse)
def final():
    return templates.TemplateResponse("score_report_page.html" )
