from pymongo import MongoClient
from amadeus_api import cheapest_flight, travel_prediction, activity_prediction, on_time_prediction


HOST = 'cluster0.h46kd.mongodb.net'
USER = 'aryijq'
PASSWORD = 'practice'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'cheapest_flight'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

# flight_list = []
# city_list = ["PAR", "MAD", "FRA", "ROM", "ICN"]
# for city in city_list:
#     flight_list.extend(cheapest_flight(city, 1))

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
# collection.insert_many(flight_list)

COLL_NAME_ACT = "activity"
COLL_NAME_ONTIME = "ontime"

# act_list = []
# ontime_list = []
# city_list = ["PAR", "MAD", "FRA", "ROM", "ICN"]

# for city in city_list:
#     dict_ontime = {"Destination" : city, "Probability" : on_time_prediction(city)}
#     ontime_list.append(dict_ontime)

collection_ontime = database[COLL_NAME_ONTIME]
# collection_ontime.insert_many(ontime_list)

