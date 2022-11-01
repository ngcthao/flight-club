from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import os

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
FLIGHT_API_KEY = os.environ.get("FLIGHT_KEY")
EMAIL = os.environ.get("EMAIL_HIDDEN")
PASS = os.environ.get("PASS_HIDDEN")

sheet = DataManager(token=SHEETY_TOKEN)
sheet.get_data()
flight_finder = FlightSearch(token=FLIGHT_API_KEY)
flight_finder.iata_search(travel_cities=sheet.city)
sheet.edit_iata(travel_cities=sheet.city, city_codes=flight_finder.city_codes)

flight_finder.flight_filter(travel_code=sheet.code, travel_cost=sheet.price)

if flight_finder.flight_available:
    flight_information = FlightData(data=flight_finder.flight_info)
    notify = NotificationManager(fd=flight_information.flight)
    sheet.get_users()
    notify.send_emails(users=sheet.users, email=EMAIL, password=PASS)
else:
    print("NO FLIGHTS AVAILABLE")
