# =============================================================================
# Why 0.1 + 0.2 != 0.3 in Python (Floating Point Precision Issue)
# =============================================================================

# Floating-point numbers are not always accurate because of how they are 
# represented in computer memory.

# Computers store floating-point numbers in binary (base-2) using the 
# IEEE 754 standard. They have a limited number of bits (53 bits of precision
# for Python's float type).

# Many decimal numbers like 0.1 and 0.2 cannot be represented exactly in binary.
# They result in repeating binary fractions:
#   0.1  → 0.00011001100110011... (repeating)
#   0.2  → 0.00110011001100110... (repeating)

# Since the computer can only store a finite number of bits, it rounds off 
# these repeating digits. The stored values of 0.1 and 0.2 are slightly 
# larger than their actual values.

# When these two approximations are added, the tiny errors combine and 
# produce: 0.30000000000000004 instead of exact 0.3

# This is not a bug. It is a fundamental limitation of binary floating-point 
# arithmetic.


from decimal import Decimal

floatx = 0.1
floaty = 0.2
print(floatx+floaty) #0.30000000000000004 due to the reason described earlier. 

decx = Decimal('0.1')
decy = Decimal('0.2')
print(decx + decy)

# Decimal module lets us handle the numbers as we want to like 0.1 + 0.2 = 0.3 and not 0.30000000000000004.