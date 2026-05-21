player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 == player2:
    print("Tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:  # player1 == "paper"
    if player2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
