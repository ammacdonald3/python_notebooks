import random

p1_wins = 0
p2_wins = 0
winning_score = 2

while p1_wins < winning_score and p2_wins < winning_score:
    print(f"Player Score: {p1_wins} Computer Score: {p2_wins}")
    print(".....Rock.....")
    print(".....Paper.....")
    print(".....Scissors.....")

    p1 = input("Enter your choice: ").lower()
    if p1 == "quit" or input == "q":
        break
    rand_num = random.randint(0,2)

    if rand_num == 0:
        p2 = "rock"
    elif rand_num == 1:
        p2 = "paper"
    else:
        p2 = "scissors"

    print("The computer chose " + p2)

    if p1 == p2:
        print("TIE GAME!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("Player 1 wins!")
            p1_wins += 1
        elif p2 == "paper":
            print("The computer wins!")
            p2_wins += 1
        else:
            print("Something went wrong...")
    elif p1 == "paper":
        if p2 == "scissors":
            print("The computer wins!")
            p2_wins += 1
        elif p2 == "rock":
            print("Player 1 wins!")
            p1_wins += 1
        else:
            print("Something went wrong...")
    elif p1 == "scissors":
        if p2 == "rock":
            print("The computer wins!")
            p2_wins += 1
        elif p2 == "paper":
            print("Player 1 wins!")
            p1_wins += 1
        else:
            print("Something went wrong...")
    else:
        print("Something went wrong...")

if p1_wins > p2_wins:
    print("CONGRATS, YOU WON!")
elif p1_wins == p2_wins:
    print("It WAS a tie game until you quit prematurely...")
else:
    print("YOU LOST to the computer...")
print(f"FINAL SCORE...Player Score: {p1_wins} Computer Score: {p2_wins}")