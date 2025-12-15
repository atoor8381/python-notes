listtwo = ["one","two","three"]

listtwo.insert(1,"1")

print(listtwo)

if "two" in listtwo : 
    print("Yeah Yeah Yeah")


################################################

listone = ["one","two","three","four"]

listone[1:2] = "meow"

print(listone)
# in this way we get each character of the meow letter seperately if we dont want that 
# we can put the entity which we want there as ["meow"]
# the reason behind this is that the python expects something itteratable to be put there in 
# the list so it itterates through the string and put each character seperately if we want a single 
# character then we can put an array with a single character. 


####################################################

#creating a copy of the list and providing it to the other variable. 

listthree = ["USA","PAK","IND"]

listthreecopy = listthree.copy() 
#by this method a copy of the listthree is provided to the listthreecopy
# if we dont use the copy method the variable will just point to the already 
#existing list in the memory so in that case both the variables will be pointing to the 
#same list. 

#######################################################
squarednum = [x**2 for x in range(10)]
print(squarednum)