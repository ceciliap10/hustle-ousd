# Lab 3 Cecilia Palau

#food string

food = "Pupusas de Frijol"

print(food[0:3])
print (food[-3:])

first_last= food[0] + food[-1]

print(first_last)

food_list= food.split()

print(food_list)

joined_food= ''.join(food_list)

#Lists

number_list= [2,10,20,100,15]

number_list.append(4)

print(number_list)

number_list.insert(3,"element")

number_list.pop(1)

number_list.remove(number_list[1])

print (number_list [0:3])
print (number_list [-3:])

#Dictionaries

books = {"Elisabetta Dami": "Four Mice Deep in the Jungle","Dr.Seuss": "Cat In The Hat", "Erik Carle":"The Very Hungry Catepillar", "Marcus Pfister": "The Rainbow Fish"}


print(books.keys ())
print(books.values ())
print(books.get("Erik Carle"))
print(books.pop("Dr.Seuss"))
del books ["Elisabetta Dami"]
