def coinMachine():
    billAmount = int(input("Please insert a bill in the folowing amounts: 1, 5, 10 , 20 "))
    if billAmount == 1:
        print("dispencing 4 quarters.")
    elif billAmount == 5:
        print("dispencing 20 quarters.")
    elif billAmount == 10: 
        print("dispencing 40 quarters.")
    elif billAmount == 20: 
        print("dispencing 80 quarters.")
    else: 
        print("sorry, this bill amount is not accepting")

coinMachine()