low = 0
high = 100
user_answer = ''

print("Please think of a number between 0 and 100!")
while user_answer != 'c':
    guess = int((low + high) / 2)
    print("Is your secret number " + str(guess) + "?")
    user_answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_answer not in ['c','h','l']:
        print("Sorry, I did not understand your input.")
    elif user_answer == 'h':
        high = guess
    elif user_answer == 'l':
        low = guess
print("Game over. Your secret number was: " + str(guess))