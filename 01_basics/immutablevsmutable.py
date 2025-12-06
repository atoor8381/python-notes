# a common perception is that the immutable objects are the ones which 
# dont allow the changes in them after they are created and anychange to 
# them result in the creation of the new object.
# the mutable object is one which allow changes to it after it was created 
# initialized. and this is correct lets understand it deeply

# Here we are creating an integer object and then we will see how the changes to this object
# result in the creation of new object.

a = 10;

# now under the hood an object of lets say 10 is created and the reference is provided 
# to the 'a'.

# now lets provide this object 10 to another variable and then make changes and see what happens:

y=a #in this case the y is also provided with the reference of the 10 object.

print(a)
print(y)

#lets make a change to the a.

a=13 
# now in the line number 24 a new object is created the reference to that is given to the a.
# the old 10 object is garbage in other cases but in this case that object is given to y.


print(a)
print(y) # y is still pointing to the old 10 object and the a is pointing to the new 13 object.


# but in the cases of the list we can make changes to the old objects...