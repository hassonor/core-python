from shipping import *

c1 = ShippingContainer("OH", ["books"])
print(c1.owner_code)
print(c1.contents)

c2 = ShippingContainer("ESC", ["pharmaceuticals"])
print(c2.serial)

c3 = ShippingContainer("ESC", ["pasta"])
print(c3.serial)
