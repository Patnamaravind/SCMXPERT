# from fastapi import APIRouter, Depends, HTTPException,Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from routes.login import get_current_user

# route=APIRouter()
# html = Jinja2Templates(directory = "Templates")
# route.mount("/project", StaticFiles(directory="project"), name = "project")

# # Route to display the dashboard page
# @route.get("/dashboard")
# def sign(request: Request):
#     return html.TemplateResponse("dasboard.html", {"request": request})

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

route = APIRouter()
html = Jinja2Templates(directory="Templates")

# Route to display the dashboard page
@route.get("/dashboard")
def sign(request: Request):
    return html.TemplateResponse("dasboard.html", {"request": request})

