str = " Meow Meow "

print(str.strip())
print(str) 
# Remember one thing that when a method is applied to the python string
# the original string does not change it stays the same bcz strings are immutable. 

str_two = "Hello"

print(str_two.replace("H","Y")) # here a string object is created but it does not get stored 
# in any variable unless we explicitly store it. 

print(str_two)


# .split can be used in order to convert the string to the list in python.

coffee_type = "Cold Coffee"
quantity = 3
str_three = "I ordered {} cups of {}"
print(str_three.format(quantity, coffee_type))

equipments = ["bat", "rackets"]
print(", ".join(equipments) ) #this will convert the equipments list to a string

