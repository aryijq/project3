from pymongo import MongoClient
from amadeus_api import cheapest_flight, travel_prediction, activity_prediction, on_time_prediction


HOST = 'cluster0.h46kd.mongodb.net'
USER = 'aryijq'
PASSWORD = 'practice'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'cheapest_flight_2'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]

COLL_NAME_ACT = "activity"
COLL_NAME_ONTIME = "ontime"

collection_ontime = database[COLL_NAME_ONTIME]

# cheapest_flight mongoDB 삽입하는 함수 생성
def insert_flight(cheapest_flight):
    # 도시 리스트 : 런던, 파리, 마드리드, 프랑크푸르트, 로마
    city_list = ["LON", "PAR", "MAD", "FRA", "ROM"]
    for city in city_list:
        collection.insert_many(cheapest_flight(city, 1))

# cheapest_flight mongoDB 삽입
# insert_flight(cheapest_flight)







# collection.insert_many(travel_prediction)
# collection.insert_many(activity_prediction)
# collection.insert_many(on_time_prediction)