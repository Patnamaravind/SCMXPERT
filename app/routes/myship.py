from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pymongo
from routes.login import *
dburl="mongodb://localhost:27017/"
connection=pymongo.MongoClient(dburl)

projectdb=connection["aravind"]
test=projectdb["test"]

route=APIRouter()
html = Jinja2Templates(directory = "HTML")
route.mount("/project", StaticFiles(directory="project"), name = "project")


@route.get("/myship")
def sign(request: Request):
    data = test.find({})
    print(data)
    return html.TemplateResponse("myship.html", {"request": request,"data":data})
   