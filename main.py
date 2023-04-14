#import the needed libraries for certain functions.
import random
import os
import sys
import time

#start!
print("WARNING! \nThis is a work in progress prototype, everything seen here is subject to change. \nWith all that said, please enjoy.")
input("Press ENTER to continue...")

#clear the screen.
os.system('clear')

splashtexts = [
  "It's a sad day to be a Goblin.", "Don't you have better things to do?",
  "Enjoy your stay.", "Now how did you end up here of all places?"
]

print("Welcome to The Dungeon")
print(splashtexts[random.randint(0, 3)])

prompt = input(
  "\nDo you want to: \n\n1: Play a Game. \n2: Quit (Coward!) \n\nEnter a Number: "
)
os.system('clear')

if prompt == '1':
  #start the game by choosing difficulty.
  difficulty = input('Choose your difficuly: \n\n1: Easy \n2: Moderate \n3: Hard \n4: Very Hard \n\nEnter a Number: ')
  
elif prompt == '2':
  #quit the game (what a loser).
  print("k' bye.")
  time.sleep(3)
  sys.exit
  
else:
  #someone did something wrong here.
  print('guh')
  time.sleep(3)
  sys.exit

#if the player is actually playing, continue here.
os.system('clear')

#get the players name, then explain the super-duper indepth lore. :3
name = input('Name your adventurer: ')
print(
  '\nWelcome,', name,
  '\nOut of every all the adventurers in the land, you have been chosen to enter The Dungeon, and slay the horrible beast that has been terrorizing the people.'
)
time.sleep(5)
print('\nYour quest begins...')
time.sleep(3)
print('NOW!')
time.sleep(2)
os.system('clear')

#define the kinds of rooms you can enter in this game.
roomtypes = [
  'empty', 'empty2', 'easymonster', 'moderatemoster', 'hardmonster', 'loot',
  'chancetime'
]

#define weapons, the numbers represent 'max damage', and 'durabillity'.
shortsword = [3, 100]
club = [10, 0, 150]

#define armor, the numbers represent the following 'defense (max damage subtractable)', 'durabillty'
leatherarmor = [3, 50]

#note to self: probably should reimplement weapons and armor to work the same as monsters.

#inventory slots
inventoryslot1 = 'empty'
inventoryslot2 = 'empty'
inventoryslot3 = 'empty'
inventoryslot4 = 'empty'
inventoryslot5 = 'empty'
armorslot = leatherarmor
weapon = shortsword

#define the names, hit points, and max amount of damage each monster can do, each monster is tied to a numeric id, so if monster '0' is called, the slime is the chosen enemy.
easymonsternames = ['Slime', 'Goblin']
easymonsterhealths = [5, 10]
easymonstermaxdamages = [1, 3]

#start the adventure
print('The old wooden doors close behind you as you begin your quest.')
time.sleep(3)

#set the player's health based on difficulty.
if difficulty == '1':
  health = 200
elif difficulty == '2':
  health = 150
elif difficulty == '3':
  health = 100
elif difficulty == "4":
  health = 50

#this is importiant i promise.
room = 0
#set a random length for the game, may be scaled by difficulty later on.
totalrooms = random.randint(10, 50)
#display the current room.
print('Room', room, '/', totalrooms, '\n')

#run this loop while the player is alive and has not made it to the last room.
while room != totalrooms and health > 0:

  #tell the game we are in the next room.
  room += 1
  #pick a random roomtype from the 'roomtypes' table.
  currroomtype = roomtypes[random.randint(0, 2)]
  #clear the screen
  os.system('clear')

  #define an action for each kind of room.
  #this room is empty, there's nothing to do.
  if currroomtype == 'empty':
    
    #print the current room
    print('Room', room, '/', totalrooms, '\n')
    #tell the player what's going on.
    print('\nThe Room is empty...\n')
    #wait for the player to continue.
    input('Press ENTER to continue...')
    continue

  #again, empty.
  elif currroomtype == 'empty2':

    #print the current room
    print('Room', room, '/', totalrooms, '\n')
    #tell the player what's going on.
    print('\nThe Room is empty...\n')
    #wait for the player to continue.
    input('Press ENTER to continue...')
    continue

  #enemy monster encounter
  elif currroomtype == 'easymonster':
    
    #print the current room
    print('Room', room, '/', totalrooms, '\n')
    #tell the player what's going on.
    print('A monster appears before you!')
    #wait 3 seconds for the player to prepare themselves.
    time.sleep(3)
    #pick a random monster from the monster table.
    monster = random.randint(0, 1)
    #get the monster's information
    monstername = easymonsternames[monster]
    monstermaxdamage = easymonstermaxdamages[monster]
    monsterhealth = easymonsterhealths[monster]
    #clear the screen
    os.system('clear')

    #decide how much damage the player and the attacking monster will do to eachother. The player's max possible damage is based on the weapon they are carrying.
    youdamage = random.randint(1, weapon[0])
    monsterdamage = random.randint(1, monstermaxdamage)

    #print all the needed information about the player
    print(name, ':')
    print('Health: ', health)
    print('Defense: ', armorslot[0])
    print('Attack:', weapon[0], '\n')
    #and about the attacking monster.
    print(monstername, ':')
    print('Health:', monsterhealth, '\n')

    #do damage by reducing the health of the player and monster by the damage the other did.
    health -= monsterdamage
    monsterhealth -= youdamage

    #begin the battle
    print('The opening attack!\n')
    #tell the player how much damage they did.
    print('You attack', monstername, 'for', youdamage, 'damage.')
    #and how much damage they took.
    print(monstername, 'attacks You for', monsterdamage, 'damage.\n')
    input('Press ENTER to continue... ')


    #loop the battle until someone dies
    while monsterhealth > 0:

      #decide how much damage the player and the attacking monster will do to eachother. The player's max possible damage is based on the weapon they are carrying.
      youdamage = random.randint(1, weapon[0])
      monsterdamage = random.randint(1, monstermaxdamage)
      
      #CLEAR. THE. SCREEN.
      os.system('clear')
      
      #print all the needed information about the player
      print(name, ':')
      print('Health: ', health)
      print('Defense: ', armorslot[0])
      print('Attack:', weapon[0], '\n')
      #and about the attacking monster.
      print(monstername, ':')
      print('Health:', monsterhealth, '\n')

      #do damage by reducing the health of the player and monster by the damage the other did.
      health -= monsterdamage

      action = input('What will you do? \n1: Attack the monster. \n2: Use an item \nEnter a Number: ')
      
      #the player chose to fight the monster back.
      if action == '1':
        monsterhealth -= youdamage
        print('\nYou attack', monstername, 'for', youdamage, 'damage.')
        #ill come back once the inventory and loot is done...
      elif action == 2:
        print('ligma')

      #tell the player they got attacked.
      print(monstername, 'attacks You for', monsterdamage, 'damage.\n')
      #wait for the player's input
      input('Press ENTER to continue.')
      #continue the loop, unless the monster is dead, then you can end the loop and let the player proceed.
      continue
    #You WIN, now let the player move on...
    print('\nVictory! You have defeated your foe.')
    input('\nPress ENTER to continue.')

print('Sorry, the horrible beast is on vacation rn, thanks for playing.')