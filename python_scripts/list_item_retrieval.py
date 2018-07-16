# create a list
colors = ["red","blue","yellow","green","purple"]

# ---FOR LOOP---
for color in colors:
    print(color)

# ---WHILE LOOP---
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

# ---WHILE LOOP WITH MORE FUNCTIONALITY---
index = 0
while index < len(colors):
    print(f"Item {index}: {colors[index]}")
    index += 1