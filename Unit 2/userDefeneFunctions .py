# User defined functions - code instructions that YOU weite/ create. 

# How to write a fuynction
# part 1 - function definition
# () --> round brackets/ parameters
def welcome_message():
    print('hello good morning sir')

# part 2 - funciton invocation/ call 
welcome_message() 

def calculate():
    num1 = int(input("please type in a number: "))
    num1 += 10 
    print(num1)

calculate()

# practice 
def foodOrder(): 
    print('hambrger, chicken, sandwich, salad')
    order = input('what would you like to order')
    print(order)

foodOrder()


# Parameters and Arguments - are data that can be passed inside of a function. 


# num1 and num2 are parameters. These are placeholders for data
#P= parameter == P= placeholder

# This placeholder data is not REAL. it is interested to be a reserved for actual incoming data. 
# This is used in the function definition

def findAvg(num1, num2): 
    print(num1 + num2)

# Argumetns are REAL data in the function call 
# There must be the same number of agruments as there are parameters otherwise you will get an error. 
# Arguement == REAL data --> in court to make a arguement, you need facts. 

findAvg(10,9)

