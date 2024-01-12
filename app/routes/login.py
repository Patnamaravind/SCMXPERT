
from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database.database import signup  # Assuming signup is the MongoDB collection
from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from typing import Optional 



route = APIRouter()
html = Jinja2Templates(directory="Templates")
route.mount("/project", StaticFiles(directory="project"), name="project")

@route.get("/login")
def login(request: Request):
    return html.TemplateResponse("login.html", {"request": request})

@route.post("/login")
def login(request: Request, username: str = Form(...)):
    var = signup.find_one({"user": username})

    if var:
        token = create_access_token(data={"sub": var["user"],
                                          "email":var["email"],
                                          "role":var["role"]
                                          })
        response_content = {
            "access_token": token,
            "username": var["user"],
            "email":var["email"],
                "role":var["role"]
        }
        return JSONResponse(content=response_content, status_code=200)
    else:
        response_content = {"detail": "Invalid credentials"}
        return JSONResponse(content=response_content, status_code=401)

# from fastapi import APIRouter, Request, Form, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from jose import jwt, ExpiredSignatureError, JWTError
# from datetime import datetime, timedelta
# from database.database import *  
# from fastapi.responses import JSONResponse
# from typing import Optional 



# route = APIRouter()
# html = Jinja2Templates(directory="Templates")
# route.mount("/project", StaticFiles(directory="project"), name="project")

# @route.get("/login")
# def login(request : Request):
#     return html.TemplateResponse("login.html", {"request": request})
 

# @route.post("/login")
# def login(request : Request, username : str = Form(), password : str = Form()):
#     var = signup.find_one({ "$and" : [ {"user":username},{"password":password} ] })
#     # print(var)
#     if var:
#         token=create_access_token(data={"sub":var["user"]})
#     return JSONResponse(content={"access_token":token, "username": var["user"], "password": var["password"]}, status_code=200)
        # localStorage.setItem(key="access_token", value=token)
        # return response
    # return html.TemplateResponse("dasboard.html", {"request": request})

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
ACCESS_TOKEN_EXPIRE_MINUTES = 10

from passlib.context import CryptContext
from jose import jwt, ExpiredSignatureError, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Request, Cookie
from datetime import datetime, timedelta
from typing import Optional, Union
import os
# from dotenv import load_dotenv
from database.database import *
import secrets

# Load environment variables from a .env file
# load_dotenv()

# Create an instance of CryptContext for password hashing and verification
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class Hash:
#     def hash_password(pwd: str):   #hashing the password
#         return pwd_cxt.hash(pwd)

#     def verify_password(pwd: str, hashed_password: str):  #verify the hashed password
#         return pwd_cxt.verify(pwd, hashed_password)

# Load environment variables for JWT configuration



# OAuth2PasswordBearer for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


###### ----------function to create access token(JWT) for user authenication----------######

def create_access_token(data: dict, expires_delta:Optional[timedelta] = None):
    to_encode = data.copy()   # Make a copy of the input data dictionary
    # Calculate the token expiration time
    if expires_delta: 
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



###### ----------function decode the JWT token----------######

def decode_token(token: str):
    try:
        # Attempt to decode the provided token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})



###### ----------function to get current user from access token----------######

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        if payload and "sub" in payload and "email" in payload:
            user_data = signup.find_one({"email": payload["email"]})
            if user_data and "username" in user_data:
                return user_data
    except JWTError:
        pass

    return None
# def create_jwt_token(username: str) -> str:
#     expiration_time = datetime.utcnow() + timedelta(hours=1)
#     payload = {"sub": username, "exp": expiration_time}
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#     return token


# def decode_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired",
#                             headers={"WWW-Authenticate": "Bearer"})
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",
#                             headers={"WWW-Authenticate": "Bearer"})
#-------------------------------------------------------------------------------------------new---------------------------------------------------
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from database.database import *
# from fastapi import Request, Depends,HTTPException, status, Cookie, Response
# from fastapi import HTTPException, status
# from jose import jwt, ExpiredSignatureError, JWTError
# import asyncio
# import os
# from dotenv import load_dotenv
 
 
# # Load environment variables from a .env file
# load_dotenv()
 
# # Load environment variables for JWT configuration
# SECRET_KEY=os.getenv("SECRET_KEY")
# ALGORITHM=os.getenv("ALGORITHM")
# ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
 
# #token authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="signin")
 
# PASSWORD_HASH = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
# #Getting hashpassword,verifypassword
# class Hashpass:
#     def create_user(password: str) -> str:
#         return PASSWORD_HASH.hash(password)
   
#     def verify_password(plain_password: str, hashed_password: str) -> bool:
#         return PASSWORD_HASH.verify(plain_password, hashed_password)
 
# #Generating token
# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()    
#     # token expiration time
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     #encode the token
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
 
 
# #decode token Function
# def decode_token(token: str):
#     try:
#         #decode the provided token
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except ExpiredSignatureError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
 
 
 
# #Get user to access jwt
# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = decode_token(token)
#         if payload and "email" in payload:
#             user_data = signup.find_one({"email": payload["email"]})
#             if user_data and "username" in user_data:
#                 return {"username": user_data["username"], "email": payload["email"]}
#     except JWTError as e:
#       if "ExpiredSignatureError" in str(e):
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Token has expired",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
 
 
# #authenticating user
# async def authenticate_user(email: str, password: str):
#     loop = asyncio.get_event_loop()
#     user = await loop.run_in_executor(None, lambda: signup.find_one({"email": email}))
#     if not user or not Hashpass.verify_password(password, user['password']):
#         return False
#     return user
 
 
