from airtravel import *
from pprint import pprint as pp

f = Flight("BA777", Aircraft("G-EUPT", "Airbus A312", num_rows=22, num_seats_per_row=6))

print(f.aircraft_model())

f = Flight("BA758", Aircraft("G-RUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
# pp(f.seating)  # all seats free

f.allocate_seat("12A", "Or Hasson")
f.allocate_seat("15F", "Gil Hasson")
# f.allocate_seat("12A", "Gil Hasson") -> Will Raise an Error  "12A" already taken.
# f.allocate_seat("DD", "Gil Hasson") -> Will Raise an Error  "DD" Invalid seat place.

# pp(f.seating)  # after we allocated some seats :)

f2 = make_flight()
pp(f2.seating)
print("---------------------------------------------------------------------")
f2.relocate_passenger("12A", "15D")
pp(f2.seating)

f3 = make_flight()
print(f3.num_available_seats())

print("---------------------------------------------------------------------")

f = make_flight()
f.make_boarding_cards(console_card_printer)

print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")

f4, g = make_flights()
print(f4.aircraft_model())
print(g.aircraft_model())

print(f4.num_available_seats())
print(g.num_available_seats())

g.relocate_passenger("55K", "13G")
g.make_boarding_cards(console_card_printer)

a = AirbusA319("G-EZBT")
print(a.num_seats())

b = Boeing777("N717AN")
print(b.num_seats())
