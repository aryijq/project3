from amadeus import Client, ResponseError, Location
import pandas as pd

# Amadeus API id/pwd
amadeus = Client(
    client_id="kehVFrr18g2OECLn3oOeDjR35YA55EEy",
    client_secret="V4ywY90VGxssGUzO"
)

# 해당 도시에서 갈 수 있는 가장 싼 목적지
def cheapest_destination(name):
    dest = amadeus.shopping.flight_destinations.get(origin=name)
    dest_data = dest.data
    return dest_data

city_list = ["PAR", "MAD", "FRA", "ROM", "ICN"]

# 날짜별로 런던 출발, 목적지에 도착하는 가장 싼 티켓
def cheapest_flight(destination, adults, origin="LON"):
    start_date = pd.to_datetime("2022-03-01")
    end_date = pd.to_datetime("2022-03-31")
    date_range = pd.date_range(start_date, end_date, freq="D")

    march=[]
    for day in date_range:
        days = str(day)[:10]
        march.append(days)

    offers = []
    for date in march:

        offer = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults
            )
        offer_data = offer.data
        offers.extend(offer_data)
    return offers


# 목적지, 출발, 귀환, 검색 나라에 따른 여행 목적
def travel_prediction(destination, dep_date, return_date, origin="LON"):
    today = str(pd.Timestamp.now())[:10]
    pred = amadeus.travel.predictions.trip_purpose.get(
                    originLocationCode=origin,
                    destinationLocationCode=destination,
                    departureDate=dep_date,
                    returnDate=return_date,
                    searchDate=today).data
    return pred

# travel_prediction("MUN", "2022-03-01", "2022-03-30")
# travel_prediction("ICN", "2022-03-03", "2022-03-10")


# 해당 도시에 방문해서 할 수 있는 액티비티 TOP 10
def activity_prediction(city):
    loc = amadeus.reference_data.locations.get(keyword=city, subType=Location.ANY)
    geocode = loc.data[0]["geoCode"]

    shop_act = amadeus.shopping.activities.get(
        latitude = geocode["latitude"],
        longitude = geocode["longitude"])
    acts = shop_act.data


    act_lst = []
    for act in acts:
        act_lst.append(act["name"])
 
    return act_lst



# 해당 공항에 제때 도착할 확률
def on_time_prediction(city):
    start_date = pd.to_datetime("2022-03-01")
    end_date = pd.to_datetime("2022-03-31")
    date_range = pd.date_range(start_date, end_date, freq="D")

    march=[]
    for day in date_range:
        days = str(day)[:10]
        march.append(days)
    
    on_time=[]
    for date in march:
        pred = amadeus.airport.predictions.on_time.get(
            airportCode=city,
            date=date)
        pred_data = pred.data["result"]
        on_time.append(pred_data)
    return on_time

# on_time_prediction("ICN")





