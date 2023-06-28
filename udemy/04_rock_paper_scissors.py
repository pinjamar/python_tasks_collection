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
game_images = [rock, paper, scissors]

# Write your code below this line 👇
player_choice = (
    input("Please make a choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))
computer_choice = random.randint(1, 3)
print(f"Computer chose {game_images[computer_choice - 1]}")

if int(player_choice) == 1:
    if computer_choice == 1:
        print("Computer's choice is Rock. It's a draw!")
    elif computer_choice == 2:
        print("Computer's choice is Paper. You lost!")
    elif computer_choice == 3:
        print("Computer's choice is Scissors. You won!")

elif int(player_choice) == 2:
    if computer_choice == 1:
        print("Computer's choice is Rock. You won!")
    elif computer_choice == 2:
        print("Computer's choice is Paper. It's a draw!")
    elif computer_choice == 3:
        print("Computer's choice is Scissors. You lost!")

elif int(player_choice) == 3:
    if computer_choice == 1:
        print("Computer's choice is Rock. You lost!")
    elif computer_choice == 2:
        print("Computer's choice is Paper. You won!")
    elif computer_choice == 3:
        print("Computer's choice is Scissors. It's a draw!")

else:
    print("You chose an invalid number! You lose!")
