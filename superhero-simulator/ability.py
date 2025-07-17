#Task2 and 2.5
import random
class Ability:
    def __init__(self, name, max_damage):
   	# implement code here
       self.name = name
       self.max_damage = max_damage

    #You need self to refreance what you are creating and accesing varibles form your class
    def attack(self):
        return random.randint(0, self.max_damage) 

if __name__ == "__main__":
    fireball = Ability("Fireball", 50)
    print(fireball.attack())
