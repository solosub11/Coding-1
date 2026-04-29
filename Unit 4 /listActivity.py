customerSatisfaction = [1,2,3,4,5]

def classCost(grade):
    if grade == customerSatisfaction[0]:
        print("1/5. This was a poor class")
    elif grade == customerSatisfaction[1]:
        print("2/5. It could be better")
    elif grade == customerSatisfaction[2]:
        print("3/5. not good but not bad")
    elif grade == customerSatisfaction[3]:
        print("4/5. pretty good")
    elif grade == customerSatisfaction[4]:
        print("5/5. Excellent")
    else: 
        print("can't find value")
    
#classCost(2)



#1 The difference between the append list method and the insert list method is that an append allows us to add an item at the END
# of a list and the insert allows us to add an item ANYWHERE in a list so long as we tell it with index to pass it in. 

#2 
groceryList = ['milk', 'pizza', 'carrots', 'water', 'chicken' 'breast']
groceryList.append("eggs")
groceryList.insert(3,"juice")
print(groceryList)

#3 The methof that will organize the list from least to greatest is the sort list method. 

#4 

