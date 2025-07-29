menu = {'Pizza': 2.99, 'Burger' : 3.99, 'Hot dog' : 1.99, 'Cheese' : 0.59, 'Icecream' : 1.49, 'Churro' : 0.79, 'Soda' : 0.89}
 
#Total Price
def total_price(food2, food4):
    price2 = menu [food2]
    price4 = menu [food4]
    total = price2 + price4
    return total

#Subtracting two food items
def price_difference(food1,food2):
    price2 = menu [food2]
    price4 = menu [food2]
    difference = abs (price2 - price4)
    return difference

#Using multiplication to increase prices
def inflation(food,multiplier):
    menu[food] = menu [food] * multiplier
    return menu

#Using devision to decrees prices
def deflation(menuitem, devide):
    menu[menuitem] = menu[menuitem] / devide
    return menu

#Unique function
def discount(food2,amount):
    if amount >=  5:
        food_discount = menu[food2] / 2
        return food_discount

    else:
        return menu[food2]
        
print(discount("Soda", 7))