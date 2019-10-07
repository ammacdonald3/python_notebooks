# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:25:58 2019

@author: amac

A palindrome is a string or sequence of characters that reads the same backward and forward. For example, "madam" 
is a palindrome. Write a function that takes in a string and returns a Boolean -> True if the input string is a 
palindrome and False if it is not. An empty string is considered a palindrome. You also need to account for the 
space character. For example, "race car" should return False as read backward it is "rac ecar".

"""

def is_palindrome(input_string):
    while len(input_string) > 1:
        if input_string[0] == input_string[-1]:
            input_string = input_string[1:-1]
            is_palindrome(input_string)
        else:
            return False
    return True

print(is_palindrome(""))