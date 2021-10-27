from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

print("Would you like to be a Pirate or Ninja")
select = input("Type P for pirate, N for Ninja")
if (select == "P"):
    print("RRRR You are a Pirate")
elif (select == "N"):
    print("HIYAA You are a Ninja")

name = input("What is your name?")
if (select == "P"):
    player=Pirate(name)
    opponent=Ninja('Shawn')
elif (select == "N"):
    player=Ninja(name)
    opponent=Pirate('Jim')
isturn=True
while(opponent.health > 0 and player.health > 0):
    if (isturn):
        player.attack(opponent)
        isturn=False
    else:
        opponent.attack(player)
        isturn=True
    print(f"Your health is {player.health}")
    print(f"Your opponent health is {opponent.health}")
if (player.health > 0):
    print(f"You Won!!! You defeated {opponent.name}!")
else:
    print(f"You were killed by {opponent.name} :-(")
