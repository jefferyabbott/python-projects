from data_manager import DataManager
from flight_search import FlightSearch

google_sheet = DataManager()
flight_search = FlightSearch()

sheet_data = google_sheet.get_sheet()

# lookup IATA codes
for city in sheet_data:
    if city['iataCode'] == '':
        city['iataCode'] = flight_search.lookup_iata_code(city['city'])
        print(city)
        google_sheet.update_iata_code(city['id'], city['iataCode'])

sheet_data = google_sheet.get_sheet()
print(sheet_data)
