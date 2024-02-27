import pymongo
import secrets

# MongoDB connection URL
dburl = "mongodb+srv://aravindsvec123:4bwm2d4mPsrAubxJ@cluster0.zef7rbt.mongodb.net/"

# Establishing connection to MongoDB using MongoClient
connection = pymongo.MongoClient(dburl)
projectdb = connection["SCMXpert"]
shipment = projectdb["ShipmentData"]
signup = projectdb["signup"]

# Generating a secure random token with 32 characters
SECRET_KEY = secrets.token_hex(32)

# JWT algorithm for token encoding and decoding
ALGORITHM = "HS256"

# Expiration time for access tokens in minutes variable
ACCESS_TOKEN_EXPIRE_MINUTES = 30





