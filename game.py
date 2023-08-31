import random

choices = ["Rock", "Paper", "Scissors"]


player_score = 0
computer_score = 0


attempts = 6


while attempts > 0:

    computer = random.choice(choices)

    player = input("Rock Paper or Scissors").strip()

    if player == computer:
        print("tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, " ", player)
            computer_score += 1
        else:
            print("You win!", player, " ", computer)
            player_score += 1
    elif player == "ورقة":
        if computer == "مقص":
            print("You lose!", computer, " ", player)
            computer_score += 1
        else:
            print("You win!", player, " ", computer)
            player_score += 1
    elif player == "مقص":
        if computer == "حجر":
            print("You lose!", computer, " ", player)
            computer_score += 1
        else:
            print("You win!", player, " ", computer)
            player_score += 1
    else:
        print("Invalid selection")

    print(f"you: point {player_score}, computer {computer_score}")

    attempts -= 1


if player_score > computer_score:
    print("You win!")
elif player_score < computer_score:
    print("The computer is the winner!")
else:
    print("No winner or loser!")
