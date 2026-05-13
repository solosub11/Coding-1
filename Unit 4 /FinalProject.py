#Sebastan's school sotre 


def SchoolstoreSelection():
    print("Here are all the snacks that im selling")
    print("3.00 = large water", "4.00 = large Juice", "1.00 = chips", "2.00 = candy")
    Schoolprice = int(input('please enter the price to purchase the snacks:'))
    if Schoolprice == 1.00: 
        print("chips")
    elif Schoolprice == 3.00:
        print("large water")
    elif Schoolprice == 4.00: 
        print("large Juice")
    elif Schoolprice == 2.00:
        print("candy")
    else:
        print("Sorry, you cannot purchase this item")


SchoolstoreSelection()


    


    
