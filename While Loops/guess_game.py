import random
random_number = random.randint(1, 10)

# establish user while the user-input num doesn't equal the random num
while True:
    user_num = input("Guess a number between 1 and 10: ")
    if int(user_num) != random_number:
        if int(user_num) > random_number:
            print("Too high, try again!")
        else:
            print("Too low, try again!")
    else:
        print("You guessed it! You won!")
        again = input("Do you want to keep playing? (y/n) ")
        if again == 'n':
            break
        else:
            random_number = random.randint(1, 10)
