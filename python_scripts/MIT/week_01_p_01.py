s = 'andrewffeiuo'

vowels = 0
for x in range(len(s)):
    if s[x] in 'aeiou':
        vowels += 1

#print(f"Number of vowels: {vowels}")
print("Number of vowels: " + str(vowels))
