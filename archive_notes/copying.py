x = input("Hey how's it going? ")
while x != "stop copying me":
    # Next two lines added in to demo the break functionality
    if (x == "exit"):
        break
    print(x)
    x = input()
print("Fine, you win")
