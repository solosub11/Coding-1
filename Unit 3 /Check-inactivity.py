def Eggmarket(egg): 
    if egg < 6:
        price = 1.15
        price *= egg
        print(price)
    elif egg >= 6:
        price = 1.00
        price *= egg
        print(price)
    elif egg >= 12:
        price = 0.75 
        price *= egg 
        print(egg)
    else:
        "Sorry you can't buy more than 20 eggs"
        
        
Eggmarket(12)
