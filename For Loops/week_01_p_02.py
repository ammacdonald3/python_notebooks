# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 

s = 'oboboboaxbobbob'

bobs = 0
# =============================================================================
# for x in range(len(s) + 1):
#     if x <= (len(s) - 2):
#         if s[x] == 'b' and s[x + 1] == 'o' and s[x + 2] == 'b':
#             bobs += 1
# =============================================================================

for x in range(len(s) + 1):
    if s[x:x+3] == 'bob':
        bobs += 1

print("Number of times bob occurs is: " + str(bobs))
