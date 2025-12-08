# When we store the reference of an object inside a variable, remember:
# The variable itself does not have a datatype; the datatype belongs to the object stored in memory.

# Ref count is the number representing how many variables have a reference to this particular object.

# When no variable refers to an object, in the case of strings and numbers,
# the garbage collector does not immediately clean those objects.
# They may be kept so that if another variable needs the same kind of object, 
# Python can reuse the old one. However, we can also forcefully delete them.


# Remember: behavior differs for immutable and mutable objects.

# Immutable objects (like numbers) can be reused by Python.
# depending on Python’s optimizations (like interning for small numbers).

# Mutable objects (like lists, dictionaries, sets) behave differently.
# Reassigning a variable creates a new object, while modifying the object
# affects all references pointing to it.

# Create a new list object [1, 2, 3] and assign it to listone
listone = [1, 2, 3]  

# listtwo now refers to the same list object as listone
listtwo = listone    

# Reassign listone to a new list object [1, 2, 3]
# Now listone points to a different object
listone = [1, 2, 3]  

# Modify the first element of the new list object
listone[0] = 44      

# listone now refers to the new object: [44, 2, 3]
print(listone)      

# listtwo still refers to the old object: [1, 2, 3]
print(listtwo)      



h1 = [1,2,3]
h2 = h1[:] #now remember that here we are getting a copy so the changes made to the h1 only reflect in the h1 because h2 is copied. 

# is can be used in order to check if the two variables point to the same memory reference or not. 

print(h1 is h2 ) # false because h2 is a copy.... 