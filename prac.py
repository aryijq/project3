from amadeus import Client, ResponseError, Location
import pandas as pd

amadeus = Client(
    client_id="kehVFrr18g2OECLn3oOeDjR35YA55EEy",
    client_secret="V4ywY90VGxssGUzO"
)



def cheapest_flight(adults, origin="LON"):
    start_date = pd.to_datetime("2022-03-01")
    end_date = pd.to_datetime("2022-03-31")
    date_range = pd.date_range(start_date, end_date, freq="D")

    march=[]
    for day in date_range:
        days = str(day)[:10]
        march.append(days)

    offers = []
    offer_list = []
    city_list = ["PAR", "MAD", "FRA", "ROM", "ICN"]

    for date in march:

        for city in city_list:

            offer = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=city,
                departureDate=date,
                adults=adults
                )
            offer_data = offer.data
            offers.extend(offer_data)
        offer_list.extend(offers)
    breakpoint()
    return offer_list

cheapest_flight(1)


start_date = pd.to_datetime("2022-03-01")
end_date = pd.to_datetime("2022-03-31")
date_range = pd.date_range(start_date, end_date, freq="D")

march=[]
for day in date_range:
    days = str(day)[:10]
    march.append(days)

offers = []
offer_list = []
city_list = ["PAR", "MAD", "FRA", "ROM", "ICN"]

# for date in march:

for city in city_list:

    offer = amadeus.shopping.flight_offers_search.get(
        originLocationCode="LON",
        destinationLocationCode=city,
        departureDate="2022-03-20",
        adults=1
        )
    offer_data = offer.data
    offers.extend(offer_data)
    # offer_list.extend(offers)


len(offers)