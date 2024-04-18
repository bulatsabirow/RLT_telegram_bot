import motor

from config import MONGO_URI, MONGO_DB

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
collection = client[MONGO_DB].sample_collection
