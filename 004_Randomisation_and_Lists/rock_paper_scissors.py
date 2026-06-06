import random

print("Welcome to the Rock Paper Scissors game")
print("*" * 20)

choices = ["Rock", "Paper", "Scissors"]
choices_art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
               """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
               """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
user_choice = int(input("What do you choose? [0] Rock, [1] Paper, [2] Scissors"))
computer_choice = random.choice(choices)

print(f"You chose {choices[user_choice]}")
print(choices_art[user_choice])
print(f"Computer chose {computer_choice}")
print(choices_art[choices.index(computer_choice)])

if choices[user_choice] == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == "Scissors":
    print("You win")
elif user_choice == 1 and computer_choice == "Rock":
    print("You win")
elif user_choice == 2 and computer_choice == "Paper":
    print("You win")
else:
    print("Computer wins")