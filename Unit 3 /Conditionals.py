# Conditionals statments - A Construct that allows 
# the program to make decisions based on the input data. 

# We use the IF and ELSE Keywords to control 
# our decisions and outcomes. 

hasUmbrella = input("It's going to rain, do you have an umbrella?")

if hasUmbrella == "Yes": 
    print("Excellent. you will be dry in the rain.")
else:
    print("You are going to get your clothes wet in the wet.")

sneakerCount = int(input("How many sheos do you have in stock?"))

if sneakerCount < 10: 
    print("inventory is low, please order more sheos.")
else: 
    print("sell as many sneakers as you can.")


def userLogin():
    pw = input("what is the password?")
    storedpw = 123 
    if pw == storedpw: 
        print("Congrats you have access")
    else: 
        print("sorry access revoked")

userLogin()

# in many cases, we want our programs to provide multiple outcomes 
# based on the data reciveved. 

# The ELIF keyword, allows use to make many more conditions that 
# can give us more outcomes 

def movieSelection(): 
    print("Here are all the movie genres we have")
    print("1: horror", "2: sci-fi" , "3: romance","4: action")
    select = int(input('please enter a number for a game.'))# always comes in as a string 
    if select == 1: 
        print("Friday the 13th")
    elif select == 2: 
        print("The Matrix")
    elif select == 3: 
        print("The Notebook")
    elif select == 4: 
        print("The Avangers")
    else:
        print("Sorry, we didnt recognize your input")

movieSelection()


def rollerCoasterAdmission():
    print("How tall are you?")
