class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self, data, stops=0, stop_city=""):
        if len(data['route']) > 1:
            stops = 1
            stop_city = data['route'][-1]['cityFrom']
        self.flight = {
            "from_city": data['cityFrom'],
            "from_code": data['flyFrom'],
            "from_date": data['route'][0]['local_departure'][0:10],
            "to_city": data['cityTo'],
            "to_code": data['flyTo'],
            "to_date": data['route'][-1]['local_arrival'][0:10],
            "price": data['price'],
            "stop_overs": stops,
            "via_city": stop_city,
            "link": data['deep_link']
        }

