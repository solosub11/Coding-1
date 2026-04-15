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


def collegeOffer(GPA):
    if GPA >= 3.5: 
        print("Congrants you have been given an offer to our school.")
    elif GPA >= 2.8:
        print("Congrants you have been given a conditional offer to our school")
    else: 
        print("Unfortunately, you have not been accepted.")

collegeOffer(3.0)





