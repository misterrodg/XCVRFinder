class Location:
    def __init__(self, name: str, type: str, lat: float, lon: float):
        self.name = name
        self.type = type
        self.lat = lat
        self.lon = lon
        self.frequencies = []
        self.airports = []

    def addFrequency(self, frequency: float):
        self.frequencies.append(frequency)

    def addAirport(self, airportId: str, frequency: float, lat: float, lon: float):
        airportDict = {"id": airportId, "frequency": frequency, "lat": lat, "lon": lon}
        self.airports.append(airportDict)

    def toDict(self):
        if len(self.airports) == 0:
            del self.airports
        return self.__dict__
