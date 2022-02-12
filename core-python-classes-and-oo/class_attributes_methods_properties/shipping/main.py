from shipping import *

c = ShippingContainer.create_empty("YML")
print(c.bic)

r1 = RefrigeratedShippingContainer("MAE", ["peas"])
print(r1.bic)

r2 = RefrigeratedShippingContainer.create_empty("YML")
print(r2)
