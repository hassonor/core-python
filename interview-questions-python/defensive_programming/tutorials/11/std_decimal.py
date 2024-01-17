from decimal import *

# 11.8. Decimal Floating Point Arithmetic
print(round(Decimal('0.70') * Decimal('1.05'), 3))

print(Decimal('1.00') % Decimal('.10'))

getcontext().prec = 36
print(Decimal(1) / Decimal(7))
