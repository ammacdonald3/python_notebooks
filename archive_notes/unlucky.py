# Andrew's method:
# for x in range(1,21):
#     if (x == 4) or (x == 13):
#         print(str(x) + " is UNLUCKY!")
#     elif (x % 2) == 0:
#         print(str(x) + " is even")
#     else:
#         print(str(x) + " is odd")

# Colt's method:
for x in range(1,21):
    if (x == 4) or (x == 13):
        print(f"{x} is UNLUCKY!")
    elif (x % 2) == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")