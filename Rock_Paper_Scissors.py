import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Chose: [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again with one of the valid options!")

print(f"You chose: {player_move}")

computer_move = ''
computer_choice_random = random.randint(1,3)

if computer_choice_random == 1:
    computer_move = rock
elif computer_choice_random == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"Computer chose: {computer_move}")

if (player_move == rock and computer_move == scissors) or \
    (player_move == scissors and computer_move == paper) or \
    (player_move == paper and computer_move == rock):
        print("You win!")
elif player_move == computer_move:
    print("It's a draw.")
else :
    print("You lose!")