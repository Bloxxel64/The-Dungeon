import random
import os
import sys
import time

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
  diffeasteregg = [
    'Choose your difficuly: \n\n1: Easy \n2: Moderate \n3: Hard \n4: Very Hard \n\nEnter a Number: ',
    'Choose your difficuly: \n\n1: Easy \n2: Moderate \n3: Hard \n4: Very Hard \n\nEnter a Number: ',
    'Choose your difficuly: \n\n1: Easy \n2: Moderate \n3: Hard \n4: Very Hard \n\nEnter a Number: ',
    'Choose your difficuly: \n\n1: Soft \n2: Stiff \n3: Hard \n4: Solid \n\nEnter a Number: '
  ]
  difficulty = input(diffeasteregg[random.randint(0, 2)])
elif prompt == '2':
  print("k' bye.")
  time.sleep(3)
  sys.exit
else:
  print('guh')
  time.sleep(3)
  sys.exit

#if the player is actually playing, continue here.
os.system('clear')

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

roomtypes = [
  'empty', 'empty2', 'easymonster', 'moderatemoster', 'hardmonster', 'loot',
  'chancetime'
]

#define weapons, the numbers represent the following 'maxdamage', 'block (damage reduction)', 'durabillity'.
shortsword = [3, 1, 100]
club = [10, 0, 150]

#define armor, the numbers represent the following 'defense (max damage subtractable)', 'durabillty'
leatherarmor = [3, 50]

#inventory slots
inventoryslot1 = 'empty'
inventoryslot2 = 'empty'
inventoryslot3 = 'empty'
inventoryslot4 = 'empty'
inventoryslot5 = 'empty'
armorslot = leatherarmor
weapon = shortsword

easymonsternames = ['Slime']
easymonsterhealths = [5]
easymonstermaxdamages = [1]

print('The old wooden doors close behind you as you begin your quest.')
time.sleep(3)

if difficulty == '1':
  health = 200
elif difficulty == '2':
  health = 150
elif difficulty == '3':
  health = 100
elif difficulty == "4":
  health = 50

room = 0
totalrooms = random.randint(10, 50)
print('Room', room, '/', totalrooms, '\n')

while room != totalrooms and health > 0:
  room += 1
  currroomtype = roomtypes[random.randint(0, 2)]
  os.system('clear')
  if currroomtype == 'empty':
    print('Room', room, '/', totalrooms, '\n')
    print('\nThe Room is empty...\n')
    input('Press ENTER to continue...')
    continue

  elif currroomtype == 'empty2':
    print('Room', room, '/', totalrooms, '\n')
    print('\nThe Room is empty...\n')
    input('Press ENTER to continue...')
    continue

  elif currroomtype == 'easymonster':
    print('Room', room, '/', totalrooms, '\n')
    print('A monster appears before you!')
    time.sleep(3)
    monster = random.randint(0, 0)
    monstername = easymonsternames[monster]
    monstermaxdamage = easymonstermaxdamages[monster]
    monsterhealth = easymonsterhealths[monster]
    while monsterhealth > 0:
      os.system('clear')
      youdamage = random.randint(1, weapon[0])
      monsterdamage = random.randint(1, monstermaxdamage)
      print(name, ':')
      print('Health: ', health)
      print('Defense: ', armorslot[0])
      print('Attack:', weapon[0], '\n')
      print(monstername, ':')
      print('Health:', monsterhealth, '\n')
      health -= monsterdamage
      monsterhealth -= youdamage
      print('You attack', monstername, 'for', youdamage, 'damage.')
      print(monstername, 'attacks You for', monsterdamage, 'damage.\n')
      input('Press ENTER to continue...')
      continue

    input('Press ENTER to continue...')
    continue
