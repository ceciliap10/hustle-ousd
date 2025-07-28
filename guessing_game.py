#This is my guessing game file/Cecilia Palau
import random
#Step2
def generate_random_number():
    return random.randint(1,100)
#Step3
#This is a loop making asking the user for a number bettween 1 and 100, and if the user gives a number out of range, its asks for them to give another.
def get_user_guess(): 
   while True:
    try:
       
       guess = int(input("Enter a number 1-100"))
       if guess >= 1 and guess <= 100:
          print("Good number!")
          return guess
       else:
          print("Enter valid input!")

    except ValueError:
      print("Not within range, please enter a valid number")

get_user_guess()   

#Step 4 The main game function
#This will make the user guess a random number and will tell you if you picked a number too small or large, untill you get the right number.
def play_guessing_game():
   print("Welcome to guessing game!")
   secret_number = generate_random_number()
   attemps = 0

while True:
    secret_number = generate_random_number()
    guess = get_user_guess()
    attempts += 1
    if guess < secret_number:
      print("That number is too small, try again!")
    
    elif guess > secret_number:
        print("The number is too high, try again!")
    else:
        print(f"Good job you guessed the secret number!")
        break 
    
#Step5
#This is asking the user if they wnat to play again or not.
def game_loop():
    while True:
      play_guessing_game()
      play_again = input("Want to play again? (Yes or No) : ").lower()
      if play_again != "NO":
         print("Thanks for playing")
         break
#Step6
#This is the code needed ro run the game!
if __name__ == "__main__": 
    game_loop()
 




   