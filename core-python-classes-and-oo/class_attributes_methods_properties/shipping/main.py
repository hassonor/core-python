from shipping import *

c = ShippingContainer.create_empty("YML", length_ft=20)
print(c.volume_ft3)

r = RefrigeratedShippingContainer.create_empty("YML", length_ft=20, celsius=-10)
print(r.volume_ft3)
