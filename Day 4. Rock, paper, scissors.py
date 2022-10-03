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


import random

todos = [rock, paper, scissors]
player = int(input("What do you chose? Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS: "))
computer = random.randint(0, 2)
if player < 0 or player > 2:
    print("Choose again")
else:
    print(f"\nYOU:\n{todos[player]}")
    
    print(f"\nCOMPUTER:\n{todos[computer]}")


if (player == 0 and computer == 0) or (player == 1 and computer == 1) or (player == 2 and computer == 2):
    print("TIE")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("YOU LOSE")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("YOU WIN")


