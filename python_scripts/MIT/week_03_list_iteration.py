L = [5, 4, 9, 1, 3]

# Method 1:
total = 0
for i in range(len(L)):
    total += L[i]
print(total)


# Method 2:
total = 0
for i in L:
    total += i
print(total)