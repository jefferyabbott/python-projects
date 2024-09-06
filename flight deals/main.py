from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import time
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet()

ORIGIN_CITY = "LON"

# update airport codes in spreadsheet
for city in sheet_data:
    if city['iataCode'] == '':
        city['iataCode'] = flight_search.lookup_iata_code(city['city'])
        data_manager.update_iata_code(city['id'], city['iataCode'])
        time.sleep(2)

# search for flights
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}.")
    flights = flight_search.check_flights(
        ORIGIN_CITY,
        destination['iataCode'],
        from_time = tomorrow,
        to_time = six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: {cheapest_flight.price}")
    time.sleep(2)



