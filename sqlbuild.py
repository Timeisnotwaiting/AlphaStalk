from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import os

MONGO = os.getenv("MONGO_DB_URL")

mongo = MongoClient(MONGO)

db = mongo.STALK
