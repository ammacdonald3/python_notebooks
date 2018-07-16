print(".....Rock.....")
print(".....Paper.....")
print(".....Scissors.....")

p1 = input("Enter Player 1's choice: ")
print("*** NO CHEATING *** \n" * 20)
p2 = input("Enter Player 2's choice: ")

print("SHOOT!")

if p1 == p2:
    print("TIE GAME!")
elif p1 == "rock":
    if p2 == "scissors":
        print("Player 1 wins!")
    elif p2 == "paper":
        print("Player 2 wins!")
    else:
        print("Something went wrong...")
elif p1 == "paper":
    if p2 == "scissors":
        print("Player 2 wins!")
    elif p2 == "rock":
        print("Player 1 wins!")
    else:
        print("Something went wrong...")
elif p1 == "scissors":
    if p2 == "rock":
        print("Player 2 wins!")
    elif p2 == "paper":
        print("Player 1 wins!")
    else:
        print("Something went wrong...")
else:
    print("Something went wrong...")
