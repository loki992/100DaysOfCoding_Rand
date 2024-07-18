import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_weapon = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_weapon = random.randint(0,2)
weapons=[rock, paper, scissors]
print(weapons[player_weapon])
print("Computer chose: ")
print(weapons[comp_weapon])
if player_weapon == comp_weapon:
    print("It's a draw!")
elif ((player_weapon == 0 and comp_weapon == 2) or (player_weapon==1 and comp_weapon == 0) or (player_weapon==2 and comp_weapon==1)):
  print("You win!")
else:
  print("You lose!")

