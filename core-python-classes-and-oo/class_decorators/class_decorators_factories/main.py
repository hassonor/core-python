from itinerary import *
from location import *

tel_aviv = Location("Tel Aviv", EarthPosition(22.12, 102.16))
new_york = Location("New York", EarthPosition(12.12, 105.16))
moscow = Location("Moscow", EarthPosition(13.12, 101.16))
kiev = Location("Kiev", EarthPosition(14.12, 100.16))
torino = Location("Torino", EarthPosition(11.12, 108.16))
beijing = Location("Beijing ", EarthPosition(87.12, 111.16))

trip = Itinerary.from_location(tel_aviv, new_york, moscow, kiev)

print(trip)
print(trip.locations)
print(trip.origin)
print(trip.destination)
print("<><><><><><><><><><><><><>")

trip.add(torino)
trip.add(beijing)
print(trip)

print("<><><><>Removing Kiev<><><><>")
trip.remove("Kiev")
print(trip)

print("<><><><>Truncate_at Moscow<><><><>")
trip.truncate_at("Moscow")
print(trip)

# trip2 = Itinerary.from_location(moscow) -> Will Raise RuntimeError

# trip3 = Itinerary.from_location(tel_aviv) -> Will Raise RuntimeError

# trip4 = Itinerary.from_location(tel_aviv, tel_aviv) -> Will Raise RuntimeError (duplicate)
