pocket = int (input("Enter pocket no (0-36): "))



if (pocket < 0 or pocket > 36):
    print("Error: Pocket no is out of range (0-36), please retry....")
elif (pocket == 0):
    print ("Pocket color: GREEN")
elif ( (pocket >= 1 and pocket <= 10) or (pocket >= 19 and pocket <= 28)):
    if (pocket%2 == 0):
        print ("Pocket color: RED")
    else:
        print ("Pocket color: BLACK")
else:
    if (pocket%2 != 0):
        print ("Pocket color: RED")
    else:
        print ("Pocket color: BLACK")