# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:15:14 2019

@author: amac
"""

print("Please think of a number between 0 and 100!")


guess = 0
response = 'h'
high = 100
low = 0

while response != 'c':
    if response == 'h' or response =='l':
        guess = (high+low) // 2
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")
    
