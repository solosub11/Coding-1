savings = 0 
goal = 1000

while savings < goal: 
    print("you currently have:"+ str(savings))
    deposit = int(input("How much do you want to add?"))
    savings += deposit 
    print("you have" + str(savings) + "in your account")
    if savings >= goal: 
        print("Congrats! you have enough for your trip")
    else: 
        print("keep saving.")





def pwLoop():
    pw = "1234abcd"
    while pw != userPw:
        print("please try again")
    userPw = input("what is your password: ")
    if pw == userPw: 
        print("congrats")

pwLoop()
