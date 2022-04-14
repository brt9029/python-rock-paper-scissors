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
print("Choose one of the following: Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
choice = input()
if choice == "0":
  print(rock)
elif choice =="1":
  print(paper)
else:
  print(scissors)
computer_choice = str(random.randint(0,2))
print("Computer chose:")
if computer_choice == "0":
  print(rock)
elif computer_choice =="1":
  print(paper)
elif computer_choice == "2":
  print(scissors)
  
if choice == "0" and computer_choice == "2":
  print("You win!")
elif choice == "1" and computer_choice == "0":
  print("You win!")
elif choice == "2" and computer_choice == "1":
  print("You win!")
elif choice == computer_choice:
  print("It's a draw.")
else:
  print("You lose.")