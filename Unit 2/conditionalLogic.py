# Conditional Logic - a special class of function that 
# lets use run specific instructions based on specific data


# We use the If and else keywords to run different 
# indtructions 

# Conditional syntax - how to write a conditional block 
absences = 0 

if absences == 0:
    print("you have a dress down day")
    # if is the condition we are looking for 
else: 
    print("you muust come in uniform")
    # else is your deafult/ exit. What we wan to happen 
    # if we CANT find the data we are looking for. 


creditsToPass = 30 

currentCredits = int(input("how many credits do you have"))

if currentCredits < creditsToPass:
    print("sorry you do not have enough credits")
else: 
    print("congrats you are graduating this year")

schoolYear = input("what year of High School are you in? ")

if schoolYear == "Freshman": 
    print("You will be taking intro to high school and you have to do certain thing")
elif schoolYear == "Sophmere":
    print("you have to take state testing")
elif schoolYear == "Junior":
    print("you need an internship")
else: 
    print("Sorry this information does not apply to you?")