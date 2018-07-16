print(".....Rock.....")
print(".....Paper.....")
print(".....Scissors.....")

p1 = input("Enter Player 1's choice: ")
p2 = input("Enter Player 2's choice: ")

print("SHOOT!")

if (p1 == "rock") and (p2 == "scissors"):
    print("Player 1 wins!")
elif (p1 == "paper") and (p2 == "scissors"):
    print("Player 2 wins!")
elif (p1 == "scissors") and (p2 == "rock"):
    print("Player 2 wins!")
elif (p1 == "scissors") and (p2 == "paper"):
    print("Player 1 wins!")
elif (p1 == "paper") and (p2 == "rock"):
    print("Player 1 wins!")
elif (p1 == "rock") and (p2 == "paper"):
    print("Player 2 wins!")
elif p1 == p2:
    print("TIE GAME!")
else:
    print("Something went wrong...")