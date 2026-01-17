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

random_choice = random.randint(0 ,2)
rock_paper_scissors = [rock, paper, scissors]
user_input = input("Make you choice: 0 for Rock, 1 for Paper and 2 for Scissors.\n")

#This is the user choice
if user_input == "0":
    print("You chose Rock")
    print(rock_paper_scissors[0])
    print(rock_paper_scissors[random_choice])
elif user_input == "1":
    print("You chose Paper")
    print(rock_paper_scissors[1])
    print(rock_paper_scissors[random_choice])
elif user_input == "2":
    print("You chose Scissors")
    print(rock_paper_scissors[2])
    print(rock_paper_scissors[random_choice])
else:
    print("Invalid Selection, Please choose either 0, 1 or 2")

#What happens when the computer chooses Rock
if rock_paper_scissors[random_choice] == rock and user_input == "0":
    print("Computer chose Rock")
    print("It's a draw!")
elif rock_paper_scissors[random_choice] == rock and user_input == "1":
    print("Computer chose rock")
    print("You Win!")
elif rock_paper_scissors[random_choice] == rock and user_input == "2":
    print("Computer chose rock")
    print("You Lose!")

#What happens when the computer chooses Paper
if rock_paper_scissors[random_choice] == paper and user_input == "0":
    print("Computer chose Paper")
    print("You Lose!")
elif rock_paper_scissors[random_choice] == paper and user_input == "1":
    print("Computer chose paper")
    print("It's a draw!")
elif rock_paper_scissors[random_choice] == paper and user_input == "2":
    print("Computer chose Paper")
    print("You Win!")

#What happens when the computer chooses Scissors
if rock_paper_scissors[random_choice] == scissors and user_input == "0":
    print("Computer chose Scissors")
    print("You Win!")
elif rock_paper_scissors[random_choice] == scissors and user_input == "1":
    print("Computer chose Scissors")
    print("You Lose!")
elif rock_paper_scissors[random_choice] == scissors and user_input == "2":
    print("Computer chose Scissors")
    print("It's a draw!")

#print(rock_paper_scissors[random_choice])