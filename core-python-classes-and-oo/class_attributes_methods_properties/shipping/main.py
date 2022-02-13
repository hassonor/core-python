from shipping import *

c = ShippingContainer.create_empty("YML", length_ft=20)
print(c.volume_ft3)

r = RefrigeratedShippingContainer.create_empty("YML", length_ft=20, celsius=-10)
print(r.volume_ft3)

h1 = HeatedRefrigeratedShippingContainer.create_empty("YML", length_ft=40, celsius=0)
print(h1.celsius)

# h1.celsius = 30 -> Too Hot

# h1.celsius = -30 -> Too Cold
