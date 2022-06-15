from pymongo import MongoClient
from amadeus_api import cheapest_flight, travel_prediction, activity_prediction, on_time_prediction


HOST = 'cluster0.h46kd.mongodb.net'
USER = 'aryijq'
PASSWORD = 'practice'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'cheapest_flight'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

COLL_NAME_ACT = "activity"
COLL_NAME_ONTIME = "ontime"

collection_ontime = database[COLL_NAME_ONTIME]
