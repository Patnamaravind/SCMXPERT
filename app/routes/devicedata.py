from fastapi import APIRouter, Request, Depends, HTTPException, status, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from routes.login import decode_token, signup, OAuth2PasswordBearer, get_current_user

client = MongoClient('mongodb+srv://aravindsvec123:4bwm2d4mPsrAubxJ@cluster0.zef7rbt.mongodb.net/')  # Replace with your MongoDB connection string
db = client['SCMXpert']  # Replace with your MongoDB database name
collection = db['DeviceData']

route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@route.get("/devicedata")
def sign(request: Request):
    return html.TemplateResponse("DeviceData.html", {"request": request})

# Route to get device data based on Device_ID
@route.post("/devicedatafirst")
async def get_device_data(request: Request, token: str = Depends(get_current_user)):
    try:
        if token:
            data1 = await request.json()
            device_id = data1.get("Device_ID")
            if device_id:
                # Assuming you want to filter data based on the received device_id {"Device_ID": device_id}
                ship_data = list(collection.find({'Device_ID': int(device_id)}, {'_id': 0}))
                if ship_data:
                    return JSONResponse(content={"data": ship_data}, status_code=200)
            return HTTPException(status_code=400, detail="Device Data Not Found")
    except HTTPException as http_error:
            return JSONResponse(content={"error_message": http_error.detail})





