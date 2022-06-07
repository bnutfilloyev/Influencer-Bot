from aiogram.contrib.fsm_storage.mongo import MongoStorage
from pymongo import MongoClient

from data.config import IP

client = MongoClient(IP)
storage = MongoStorage()

database = client["InfluencerBot"]

users = database["users"]
