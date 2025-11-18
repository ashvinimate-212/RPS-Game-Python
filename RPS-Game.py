import random

options = ["rock", "paper", "scissors"]

user = input("Enter rock/paper/scissors: ")
computer = random.choice(options)

print("Computer:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
