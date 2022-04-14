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
game_images = [rock, paper, scissors]
print("Choose one of the following: Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
choice = int(input())
print(game_images[choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])
  
if choice == 0 and computer_choice == 2:
  print("You win!")
elif choice == 1 and computer_choice == 0:
  print("You win!")
elif choice == 2 and computer_choice == 1:
  print("You win!")
elif choice == computer_choice:
  print("It's a draw.")
else:
  print("You lose.")