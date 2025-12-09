# Integers, floats, Decimals, and Fractions are stored in different internal formats in memory, but conceptually they are all classified as numbers 
# because they represent numeric values and support arithmetic operations.

# why do we need the decimal module when have the built in fuctionality for the float in the python.

# When we assign a float in Python, it is converted into binary and stored using the 64-bit IEEE-754 format, where 52 bits are for the mantissa in 1.
# xxxx form and 11 bits are for the exponent, which tells how much to shift the binary point. Because 0.1 becomes an infinite repeating binary number, 
# it gets approximated, which causes inaccurate results like 0.30000000000000004. The Decimal module avoids this by doing base-10 arithmetic instead of 
# base-2 floating-point arithmetic.

from decimal import Decimal

floatx = 0.1
floaty = 0.2
print(floatx+floaty) #0.30000000000000004 due to the reason described earlier. 

decx = Decimal('0.1')
decy = Decimal('0.2')
print(decx + decy)

