from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.login import *

route=APIRouter()
html = Jinja2Templates(directory = "HTML")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/devicedata")
def sign(request: Request):
    return html.TemplateResponse("devicedata.html", {"request": request})