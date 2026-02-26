# built in functions - code intructions that are built-in to the programing language. usually locked away behind a keyword. 


# print - is a built in function that lets us printount data in the terminal =. 
print("Sebastian Hernandez")
print(2+2)


message = "this is a message that I wrote in Python"

print(message)

# input() - is a built in function that aloows us to type in (put in) data trhpugh the terminal. to use input it must be ASSIGNED to a varibale. 

name = input("please type in your name:") 
print(name)

# Data-casting BUILT in Functions (Data Conversation)
# Datacasting are functions that allow us to change data types. 

# str() - this built in function will change whatever is in the round brackets into a string. 

number = 100 
print(type(number)) # class int = integer
print(type(str(number))) # class str = string 

# int() - this built in function will change whatever is in the round brackets into a integer (whole number)

number = "100"
print(type(number)) #class int = string 
print(type(int(number))) # class int = integer

# float() - built in function will change whatever that's in the round brackets into a float (decmial number)

number = 100
print(type(number)) #class int = integer
print(type(float(number))) # class int = integer

# bool() - this built in function will change whatever is in the round brackets into a boolean (true/ false) value 

number = 100
print(type(number)) #class int = integer
print(type(bool(number))) # class int = integer --> True 


answer = input('please type in a number') # input ALWAYS takes data as a string 
print(4 * int(answer))

order = 30 
print('hey Tom, we need to order' + str(order) + ' boxes of pencils')