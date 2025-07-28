#lab5 Cecilia Palau

#step 1
def cat_greeting(word):
    print(f'Cat says {word} its nice to meet you! My friend the dog only says woof.')
    print(f'Dog says {word}')

cat_greeting("meow")
cat_greeting("woof")


#step 2  
# Fixed inputs  
def generate_superhero_power1():
    name = "Johnny"
    power = "flying"
    print(f"{name}'s power is {power}")

generate_superhero_power1()

 #step 3
 #fixed inputs
def generate_superhero_power1():    
    power = "flying"
    return power

print(generate_superhero_power1())
 
#step 4
#flexible inputs
def generate_superhero_power2(user_name,super_power):
    message = user_name +  "has the power of" +  super_power + "!" +  "She loves to speak to all of her pets!"
    return message

print(generate_superhero_power2("Cecilia", "Speak to animals")) 

#step 5
def cat_greetings_loop(greeting):
    greeting = ["meow", "purr", "scratch"]
    #Can also jut put 5
    for i in range(0,5):
        print(f'The cat says {greeting}')
greeting = ["meow", "purr", "scratch"]        
cat_greetings_loop(greeting)        

#can also do a little more understandable: 
# def cat_greeting_loop():
#greeting = ["meow", "purr", "woof"]
#for i in greetings:
#print("The cat says", i)

#step 6 
def generate_multiple_superpowers(powers):
    for i in powers:
        print(i)

powers_list = ["Breathing under water", "Teleporting", "Speaking to animals"]

generate_multiple_superpowers(powers_list)#calling function with argument