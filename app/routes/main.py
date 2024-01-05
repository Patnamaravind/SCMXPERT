
# # from fastapi import Depends, HTTPException, status, FastAPI,APIRouter
# # from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# # from jose import JWTError, jwt
# # from datetime import datetime, timedelta
# # from pymongo import MongoClient
# # from passlib.context import CryptContext
# # from typing import List
# # from database.database import *

# # route=APIRouter()

# # # MongoDB connection
# # client = MongoClient("mongodb://localhost:27017")
# # db = client["aravind"]
# # users_collection = db["signup"]

# # # Security configurations
# # SECRET_KEY = "your-secret-key"
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 30
# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # # Password hashing
# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # # Function to get user from the database
# # async def get_user(username: str):
# #     user = signup.find_one({"user": username})
# #     return user

# # # Function to authenticate user
# # async def authenticate_user(username: str, password: str):
# #     user = await get_user(username)
# #     return user

# # # Function to create JWT access token
# # def create_access_token(data: dict, expires_delta: timedelta):
# #     to_encode = data.copy()
# #     if expires_delta:
# #         expire = datetime.utcnow() + expires_delta
# #     else:
# #         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Default expiration time
# #     to_encode.update({"exp": expire})
# #     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
# #     print("encoded",encoded_jwt)
# #     return encoded_jwt

# # async def get_current_user(token: str = Depends(oauth2_scheme)):
# #     credentials_exception = HTTPException(
# #         status_code=status.HTTP_401_UNAUTHORIZED,
# #         # detail="Could not validate credentials",
# #         headers={"WWW-Authenticate": "Bearer"},
# #     )
# #     try:
# #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# #         username: str = payload.get("sub")
# #         if username is None:
# #             raise credentials_exception
# #     except JWTError:
# #         raise credentials_exception
# #     user = await get_user(username)
# #     if user is None:
# #         raise credentials_exception
# #     return user
# # @route.get("/")
# # def login():
# #     return {"hi":"hi"}

# # @route.post("/token")
# # async def login_for_access_token(user):
# #     if not user:
# #         raise HTTPException(
# #             status_code=status.HTTP_401_UNAUTHORIZED,
# #             detail="Incorrect username or password",
# #             headers={"WWW-Authenticate": "Bearer"},
# #         )

# #     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# #     access_token = create_access_token(
# #         data={"sub": user["user"],"password":user["password"], "expires_delta":access_token_expires}
# #     )
# #     print(access_token)
# #     return {"access_token": access_token, "token_type": "bearer"}




# from fastapi import Depends, HTTPException, status, FastAPI,APIRouter
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from pymongo import MongoClient
# from passlib.context import CryptContext
# from typing import List
# from database.database import *

# route=APIRouter()

# # MongoDB connection
# client = MongoClient("mongodb://localhost:27017")
# db = client["aravind"]
# users_collection = db["signup"]

# # Security configurations
# SECRET_KEY = "your-secret-key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Function to get user from the database
# async def get_user(username: str):
#     user = signup.find_one({"user": username})
#     return user

# # Function to authenticate user
# async def authenticate_user(username: str, password: str):
#     user = await get_user(username)
#     return user

# # Function to create JWT access token
# def create_access_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Default expiration time
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     print("encoded",encoded_jwt)
#     return encoded_jwt

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         # detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = await get_user(username)
#     if user is None:
#         raise credentials_exception
#     return user

# @route.get("/")
# def login():
#     return {"hi":"hi"}

# @route.post("/token")
# async def login_for_access_token(user):
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user["user"],"password":user["password"], "expires_delta":access_token_expires}
#     )
#     print(access_token)
#     return {"access_token": access_token, "token_type": "bearer"}


