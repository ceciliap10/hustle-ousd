#I want a program that will create, delet, update and read.

cookbook = [] 

def create(recipie):
    cookbook.append(recipie)
    print(f"The recipie {recipie} has been added to your cookbook!")
    #f string is used to print out a list to add additional words

def read(index):
    if index < len(cookbook):#Checks if its in range
        return cookbook[index] #The index will change depending on where we are in the list
    else:
        print("Please pick an index within range")


def update(index, recipie):
    cookbook.append(recipie)
    print(f"The recipie {recipie} has been updated in your cookbook")

def destroy(index):
    if index < len(cookbook):
        cookbook.remove(index)
        print(f"The recipie {index} has been removed for your cookbook")
    else:
        print("Please pick an index within range")    

def list_all_recipies (cookbook):
      for recipie in cookbook:#Checks every item in list
          print(recipie)

#Copied from document
def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")

        list_all_recipies(cookbook)
        
        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipies(cookbook)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()
