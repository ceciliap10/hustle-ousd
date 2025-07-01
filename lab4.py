checking = "yes"

while checking == "yes":
    print("what is your age: ")
    user_input = int()#It reads it as a string without the int
    if user_input >= 18:
        print("Yes you can vote")
    else:
        print("You cant vote") 
    print("Would you like to check another age?") 
    user_input2 = input() 
    checking = user_input2

list1 = [3, -1, 0, 6, -4]    

for x in list1:
    if x > 0:
        print("Value is positive")
    elif x < 0:
        print("Value is negative")    
    else:
        print("Number is zero")

inventory = ["tnt", "glass", "grass", "netherite", "Waxed Lightly Weathered Chiseled Copper Stairs"] 

for iten in inventory:
    if i == "tnt":
       print("boom")
    elif i == "grass":
        print("green")

for i in inventory:
    if i == "diamonds":
        print("You found {i} Jackpot!")
    else:
        print("You currently have {i}")   