# FOR loop is a type of looping construct that repeats code 
# instruction a specific (finite) amount of times 

# For loop syntax 
for x in range(10):
    print("x =" + str(x))
# range() is a special function that lets us count
# sequentially upto a certain number, even at certain intervals.


# For loops work really nicely with collections such as list, because 
# we want to do something to each piece of data in the list

coworkers = ["BIll", "Mary", "Philip"]

for worker in coworkers:
    if worker == "Mary":
        coworkers.remove('Mary')
        print(coworkers)
        print(worker + 'recieve a gift card')


prices = [10,60,20.00, 40.00]

for item in prices:
    discount = 5.00 
    item <= discount
    print(item)
    