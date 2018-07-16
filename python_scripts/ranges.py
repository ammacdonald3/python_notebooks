# Python Ranges
# Arguments:
#	1. First argument - starting point (inclusive) **OPTIONAL - default is 0
#	2. Second argument - end point (exclusive)
#	3. Third argument - steps to count by **OPTIONAL - default is 1

# return integers from 0 to 6:
a = range(7)
list(a)

# return integers from 1 to 9:
b = range(1,10)
list(b)

# return odd integers from 1 to 9:
c = range(1,10,2)
list(c)

# return integers from 8 to 1:
d = range(8,0,-1)
list(d)

# example of ranges using for loop
for num in range(20,6,-2):
    print(num)

# add all odd numbers from 10 to 20 (inclusive):
x = 0
for i in range(11,21,2):
    x += i
print(x)