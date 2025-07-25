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
print("Welcome to the Rock! Paper! Scissors! Game.")
print()

## the user
user = input("chose 'r' for rock, 'p' for paper, 's' for sciessors: ")
if user == 'r':
    print(rock)
elif user == 'p':
    print(paper)
elif user == 's':
    print(scissors)
else:
    print("unvaild input!")


## the computer
list_of_options_r_p_s = ['r','p','s']
computer = random.choice(list_of_options_r_p_s)
print("computer:", end='')
if computer == 'r':
    print(rock)
elif computer == 'p':
    print(paper)
elif computer == 's':
    print(scissors)

## the game logic
if user == 'r' and computer == 's':
    print("###### you won ######")
elif user == 's' and computer == 'p':
    print("###### you won###### ")
elif user == "p" and computer == 'r':
    print("###### you won ###### ")
elif user == computer:
    print("tie")
else:
    print("***** you lost ***** ")