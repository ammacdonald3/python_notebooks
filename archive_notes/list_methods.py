nums = [1, 4, 2, 9, 7]

# ---APPEND---
nums.append(563)
print(nums)


# ---EXTEND---
nums.extend([45, 54, 63])
print(nums)


# ---INSERT--- 
# First argument is placement in list
# Second argument is value to be inserted
nums.insert(2, 940390)
print(nums)


# ---CLEAR---
nums.clear()
print(nums)


# ---POP---
# Specify index - removes indexed value
# Don't specify index - removes last item in list
nums = [1, 4, 2, 9, 7]
nums.pop(1)
nums.pop()
print(nums)


# ---REMOVE---
# Specify value to be removed (NOT INDEX)
# Only removes first instance of value
nums = [1, 4, 2, 9, 7, 7]
nums.remove(7)
print(nums)