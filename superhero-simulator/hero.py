#Hero.py for hero profile, stroing the heros info
#Innit means 
#Task1
import random
#Taking clases from other files
from ability import Ability
from armor import Armor
from arena import Arena

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.ability = []
        self.armor_list = []

    def battle(self,opponent):
        winner = random.choice([self,opponent])
        print(f"{winner.name} wins the battle!")
    
    def add_ability(self, ability): 
        self.ability.append(ability)

    def sum_of_attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
            return total_damage

    def add_armor(self,new_armor):
        self.armor_list.append(new_armor)

    def defend(self):
        total_defense = 0
        for armor in self.armor_list:
            total_defense += armor.max_block()
            return total_defense





if __name__ == "__main__":
    hero1 = Hero("Spiderman", 1000)
    hero1.add_ability("Web shooters")
    hero1.add_armor("Web wings")
    print(hero1.abilities) 
    print(hero1.armor)    
    hero2 = Hero("Batman", 1000)
    hero1.battle(hero2)

#Random winners
import random

def battle(self, opponent):
    '''Fight another hero and randomly declare a winner'''
   #Implimentations here
    winner =  random.choice([self.winner,opponent])
    winner = random.choice([self.name,opponent])
    print(f"{winner} wins the battle") 
