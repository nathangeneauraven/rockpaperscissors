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

#Write your code below this line 👇

player_choice = int(input("Please choose 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if player_choice == 0:
  player_choice = rock
elif player_choice == 1:
  player_choice = paper
elif player_choice == 2:
  player_choice = scissors

computer_choice = random.randint(0, 2)

if computer_choice == 0:
  computer_choice = rock
elif computer_choice == 1:
  computer_choice = paper
elif computer_choice == 2:
  computer_choice = scissors

print("Player Chooses:")
print(player_choice)

print("Computer Chooses:")
print(computer_choice)

if player_choice == rock and computer_choice == paper:
  print("You Lose!")
elif player_choice == rock and computer_choice == scissors:
  print("You Win!")
elif player_choice == rock and computer_choice == rock:
  print("Draw!")
elif player_choice == paper and computer_choice == rock:
  print("You Win!")
elif player_choice == paper and computer_choice == paper:
  print("Draw!")
elif player_choice == paper and computer_choice == scissors:
  print("You Lose!")
elif player_choice == scissors and computer_choice == rock:
  print("You Lose!")
elif player_choice == scissors and computer_choice == paper:
  print("You Win!")
elif player_choice == scissors and player_choice == scissors:
  print("Draw!")
else:
  print("You entered an invalid choice. You Lose!")
