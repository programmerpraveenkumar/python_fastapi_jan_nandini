from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.api.routes import router

app = FastAPI()

app = FastAPI()
app.include_router(router)
