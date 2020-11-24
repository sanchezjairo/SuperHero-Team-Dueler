from ability import Ability
from armor import Armor
import random

class Hero:

    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''   
        winner_list = [self.name, opponent]
        winner = random.choice(winner_list)
        print(f'{winner} won!')

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
      '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
      '''

      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
      for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
      return total_damage

    def add_armor(self, armor):
        self.armors = armor

    def defend(self):
      total_block  = 0
      for Armor in self.armors:
          total_block -= Armor.defend()
      return total_block