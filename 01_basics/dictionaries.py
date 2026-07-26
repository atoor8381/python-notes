# A view object just gives us the dynamic view of the dictionary's entries 

dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

for key, value in dict.items():
    print(key, value)
    #this will print the key and value of the dictionary in a dynamic way.

Squarednums = {x:x**2 for x in range(2,5)}

print(Squarednums)