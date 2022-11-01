import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self, token):
        self.endpoint = "https://api.sheety.co/d20206f0f2fecd24c6848f9f8ea9dfe0/flightDeals"
        self.headers = {
            "Authorization": f"Bearer {token}",
        }
        self.city = []
        self.code = []
        self.price = []
        self.users = []

    def get_data(self):
        sheet_data = requests.get(url=self.endpoint+"/prices", headers=self.headers).json()
        for entry in sheet_data["prices"]:
            self.city.append(entry["city"])
            self.code.append(entry["iataCode"])
            self.price.append(entry["lowestPrice"])

    def edit_iata(self, travel_cities, city_codes):
        for num in range(0, len(travel_cities)):
            params = {
                "price": {
                    "iataCode": city_codes[num]
                }
            }
            edit = requests.put(url=f"{self.endpoint}/prices/{num+2}", json=params, headers=self.headers)

    def get_users(self):
        sheet_data = requests.get(url=self.endpoint+"/users", headers=self.headers).json()
        for entry in sheet_data["users"]:
            user = {
                "firstName": entry['firstName'],
                "lastName": entry['lastName'],
                "email": entry['email'],
            }
            self.users.append(user)