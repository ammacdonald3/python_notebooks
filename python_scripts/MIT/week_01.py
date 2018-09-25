#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:22:14 2018

@author: andrewmacdonald
"""

# STRINGS

# Concatenate strings
hi = "hello there"
name = "Andrew"
greeting = hi + ", " + name
print("STRING CONCATENATION:")
print(greeting)
print("")


# Determine length of a string
name_length = len(name)
print("STRING LENGTH:")
print(name_length)
print("")


# Extract first element from string
first_letter = name[0]
print("FIRST LETTER OF NAME:")
print(first_letter)
print("")


# Slice string
sliced_string_middle = name[2:5]
print("SLICED STRING (MIDDLE):")
print(sliced_string_middle)
print("")

sliced_string_beginning = name[:3]
print("SLICED STRING (BEGINNING):")
print(sliced_string_beginning)
print("")

sliced_string_end = name[3:]
print("SLICED STRING (END):")
print(sliced_string_end)
print("")



# INPUT and OUTPUT

# Input
#print("INPUT EXAMPLE:")
#text = input("Enter your input here: ")
#print(3 * text)
#print("")



# CONTROL FLOW

# While loop
print("WHILE LOOP:")
x = 0
while x <= 5:
    x += 1
    print(x)
print("")

#n = input("You are in the Lost Forest. Go left or right?    ")
#while n != "left":
#    n = input("You are in the Lost Forest. Go left or right?    ")
#print("You got out of the forest!")
    

# For loop
print("FOR LOOP:")
x = 0
for x in range(6):
    x += 1
    print(x)
print("")


# Break
print("BREAK:")
sum_val = 0
for z in range(5, 11, 2):
    print(sum_val)
    sum_val += z
    if sum_val == 7:
        break
print(sum_val)
print("")


# ITERATION
print("ITERATION:")
x = 24779
ans = 0
iters_left = x
while iters_left != 0:
    ans += x
    iters_left -= 1
print(str(x) + "*" + str(x) + " = " + str(ans))
print("")

# GUESS AND CHECK
print("GUESS AND CHECK - CUBE ROOT #1:")
x = -125
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of " + str(x) + " is " + str(ans))

print("")

print("GUESS AND CHECK - CUBE ROOT #2:")
cube = 9
for guess in range(cube + 1):
    if guess**3 >= cube:
        break
if guess**3 != cube:
    print(str(cube) + " is not a perfect cube")
else:
    print("Cube root of " + str(cube) + " is " + str(guess))

print("")