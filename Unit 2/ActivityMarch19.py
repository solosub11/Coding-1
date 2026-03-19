# 1. In your own words, what is the difference between a function parameter and a function argument?
# Please write your resonse as a string data type. 
"The difference between a function parameter and a function argument is that a function parameter are placeholder for data while"
"a function argurment is REAL data in a function call."

# 2. Using what you've learned in class, create a function that will calucalte the tip amount for a dinner. 
# Your function should allow the user to input the total amount of the dinner, and your tip percentage should be 
# passed in as argument. Your function should calculate and then print how much the user has to pay in tips based on the sum.

# for example if my dinner costs 100 dollars and my tip rate is 20 percent, the function should print out, 
# you owe 20.0 dollars in tips.

# If necessary, look up how to calculate a percentage.

tipamount = "the desired tip rate"
dinercost = "The total cost of the diner"

tipamount = input(dinercost * str(tipamount/100))
print("you owe the tipamount dollars in tips")

# 3. Create a function that will calculate the number of hours in a specific number of days.
# your function should take in the number of days as an argument. Your function should
# return the number of hours based on the number of days passed into it.

# for example, if I type in 3 days into my function argument, the function should print
# there are 72 hours in 3 days.

# hint you will need to use string concatenation and some datacasting functions to print out the message.


Totalhours = 72 
Numdays = 3 
input(int(3 * 24))
print(str("there are totalhours hours in numdays"))