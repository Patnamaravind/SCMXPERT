from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes.dashboard import route as dash
from routes.devicedata import route as device
from routes.login import route as log
from routes.myship import route as myship
from routes.shipment import route as shipment
from routes.signup import route as signup
from routes.startingpage import route as starting
from routes.shipment import route as data


# import pymongo
# dburl="mongodb://localhost:27017/"
# connection=pymongo.MongoClient(dburl)

# projectdb=connection["aravind"]
# test=projectdb["test"]

app=FastAPI()
html = Jinja2Templates(directory = "HTML")
app.mount("/project", StaticFiles(directory="project"), name = "project")

# @app.get("/home")
# def home():
#     return {"name":"aravind"}

# @app.get("/sign")
# def sign(request: Request):


#     data = test.find({})
#     print(data)
#     return html.TemplateResponse("myship.html", {"request": request,"data":data})
app.include_router(dash)
app.include_router(device)
app.include_router(log)
app.include_router(myship)
app.include_router(shipment)
app.include_router(signup)
app.include_router(starting)
app.include_router(data)


