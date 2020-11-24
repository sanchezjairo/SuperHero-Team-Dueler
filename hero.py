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


  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  #1) randomly choose winner,
  #Hint: Look into random library, more specifically the choice method


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)