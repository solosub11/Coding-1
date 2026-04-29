# lists are a container data type for
# sotring multiple types of data. 

# lists are useful foe keeping data, 
# organzed, structured, and space-firendly 

# List Syntax
# To create a list, we start with a name,
# followed by the assignment operator, and 
# ten square brackets. Inside the brackets 
# is where we put our data. 

blCoding = ["Intro codding", "coding 2", "ap comp sci"]
print(blCoding)


# every item in a list is called an index.
# lists are organized sequentially vy index position 
# lists always start at zero.

print(blCoding[1])

# list methods are functions that work on lists
# remeber: functions just means code instructions 

# the append method allows us to add an item at the END of a list
blCoding.append("cyber security")
print(blCoding)

# The insert method allows us to add an item ANYWHERE in a list so long as we tell it with index to pass
# it in 
blCoding.insert(2,15)
print(blCoding)




