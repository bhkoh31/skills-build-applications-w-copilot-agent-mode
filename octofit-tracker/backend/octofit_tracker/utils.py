from pymongo import MongoClient
from django.conf import settings

def get_mongo_client():
    return MongoClient(host=settings.MONGO_DB_SETTINGS["host"], port=settings.MONGO_DB_SETTINGS["port"])

def get_mongo_db():
    client = get_mongo_client()
    return client[settings.MONGO_DB_SETTINGS["db_name"]]
