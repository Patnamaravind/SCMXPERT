# from fastapi import APIRouter,Request,Form, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from database.database import *
# import pymongo
# import jwt
# import datetime

# from routes.main import *
# route=APIRouter()
# from fastapi import FastAPI, Request, Form, HTTPException
# from fastapi.responses import JSONResponse


# html = Jinja2Templates(directory = "HTML")
# route.mount("/project", StaticFiles(directory="project"), name = "project")


# from jose import jwt, ExpiredSignatureError, JWTError
# from fastapi import APIRouter,Request,status
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from database.database import *
# import jwt
# import datetime
 
# route = APIRouter()
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
# #----------------------------FUNCTION TO GENERATE THE TOKEN---------------------------------
# def create_jwt_token(username: str) -> str:
#     expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
#     payload = {"sub": username, "exp": expiration_time}
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     print(token)
#     return token





# #----------------------FUNCTION TO GET THE TOKEN FROM THE CUREEENT USER-------------------------------
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = decode_token(token)
#         if payload and "sub" in payload:
#             username = payload["sub"]
#             user_data = signup.find_one({"user": username})
#             if user_data and "user" in user_data:
#                 return {"username": user_data["user"]}
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="User not found",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
 

# @route.get("/login")
# def login(request : Request):
#     return html.TemplateResponse("login.html", {"request": request})
 
# @route.post("/login")
# def login(request : Request, username : str = Form(), password : str = Form()):
#     var = signup.find_one({ "$and" : [ {"user":username},{"password":password} ] })
#     print(var)
#     if var:
#         token=create_jwt_token(var["user"])
#         print(token)
#         return html.TemplateResponse("dashboard.html", {"request": request,"token":token})
#     return html.TemplateResponse("login.html", {"request": request})
   
 #----------------------------------------------------------------  working-----------------------------------------------------------------------------------------
# from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from jose import jwt, ExpiredSignatureError, JWTError
# from datetime import datetime, timedelta
# from database.database import signup

# route = APIRouter()
# html = Jinja2Templates(directory="HTML")
# route.mount("/project", StaticFiles(directory="project"), name="project")

# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# def create_jwt_token(username: str) -> str:
#     expiration_time = datetime.utcnow() + timedelta(hours=1)
#     payload = {"sub": username, "exp": expiration_time}
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     # print(token)
#     return token


# # #-----------------------FUNCTION TO DECODE THE TOKEN--------------------------------------------
# def decode_token(token: str):
#     try:
#         # Attempt to decode the provided token
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})


# # def get_current_user(token: str = Depends(oauth2_scheme)):
# #     try:
# #         payload = decode_token(token)
# #         if payload and "sub" in payload:
# #             username = payload["sub"]
# #             user_data = signup.find_one({"user": username})
# #             if user_data and "user" in user_data:
# #                 return {"username": user_data["user"]}
# #     except JWTError:
# #         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
# #                             detail="Invalid token",
# #                             headers={"WWW-Authenticate": "Bearer"})
# #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
# #                         detail="User not found",
# #                         headers={"WWW-Authenticate": "Bearer"})


# @route.get("/login")
# def login_page(request: Request):
#     return html.TemplateResponse("login.html", {"request": request})


# @route.post("/login")
# def login(request: Request, username: str = Form(...), password: str = Form(...)):
#     user = signup.find_one({"$and": [{"user": username}, {"password": password}]})
#     # print(user)
#     if user:
#         token = create_jwt_token(user["user"])
#         # print(token)
#         return html.TemplateResponse("dashboard.html", {"request": request, "token": token})
#     return html.TemplateResponse("login.html", {"request": request})



from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jose import jwt, ExpiredSignatureError, JWTError
from datetime import datetime, timedelta
from database.database import *  

route = APIRouter()
html = Jinja2Templates(directory="HTML")
route.mount("/project", StaticFiles(directory="project"), name="project")
@route.get("/login")
def login(request : Request):
    return html.TemplateResponse("login.html", {"request": request})
 
@route.post("/login")
def login(request : Request, username : str = Form(), password : str = Form()):
    var = signup.find_one({ "$and" : [ {"user":username},{"password":password} ] })
    # print(var)
    if var:
        token=create_jwt_token(var["user"])
        # print(token)
        return html.TemplateResponse("dashboard.html", {"request": request,"token":token})
    return html.TemplateResponse("login.html", {"request": request})

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def create_jwt_token(username: str) -> str:
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    payload = {"sub": username, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired",
                            headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})


# @route.get("/login")
# def login_page(request: Request):
#     return html.TemplateResponse("login.html", {"request": request})


# @route.post("/login")
# def login(request: Request, username: str = Form(...), password: str = Form(...)):
#     user = signup.find_one({"$and": [{"user": username}, {"password": password}]})
#     if user:
#         token = create_jwt_token(user["user"])
#         return html.TemplateResponse("dashboard.html", {"request": request, "token": token})
#     return html.TemplateResponse("login.html", {"request": request})


# Protected endpoint
@route.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        if payload and "sub" in payload:
            username = payload["sub"]
            user_data = signup.find_one({"user": username})
            if user_data and "user" in user_data:
                return {"message": "Access granted"}
    except HTTPException as e:
        raise e
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")




