import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta
FLY_FROM = "NYC"


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self, token):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": token,
            "Content - Type": "application/json",
        }
        self.city_codes = []
        self.flight_info = []
        self.flight_available = False

    def iata_search(self, travel_cities):
        for city in travel_cities:
            query = {
                "term": city
            }
            location = requests.get(url=self.endpoint+"/locations/query", params=query, headers=self.headers)
            self.city_codes.append(location.json()['locations'][0]['code'])
            # It replaces all the cities, but replacing only empty entries may be better

    def flight_filter(self, travel_code, travel_cost):
        """This function searches for available flights according to the parameters given."""
        date_today = datetime.now()
        date_future = datetime.now() + relativedelta(months=+6)
        for num in range(0, len(travel_code)):
            query = {
                "fly_from": FLY_FROM,
                "fly_to": travel_code[num],
                "date_from": date_today.strftime("%d/%m/%Y"),
                "date_to": date_future.strftime("%d/%m/%Y"),
                "price_to": travel_cost[num],
            }
            flight_response = requests.get(url=self.endpoint+"/v2/search", params=query, headers=self.headers).json()
            if flight_response["data"]:
                self.flight_info = flight_response["data"][0]
                self.flight_available = True
                break
            else:
                self.flight_available = False

