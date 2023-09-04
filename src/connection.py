from pymongo import MongoClient

from src.ConfigurationLoader import ConfigurationLoader as configuration

client = MongoClient(configuration.get_value(section="MONGODB", key="url"))

db = client.dio_live

trends_collection = db.trends
