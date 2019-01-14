

#s = 'azcbobobe'

#s = 'abcdmnope'

#s = 'abc'

# =============================================================================
# long1 = ''
# long2 = ''
# for x in range(len(s) + 1):
#     if x == 0:
#         if s[x] < s[x + 1]:
#             long1 += s[x]
#     elif x <= (len(s) - 1):
#         if s[x - 1] < s[x]:
#             long2 += s[x]
#             print("X1:" + str(x))
#             print("LONG1-1:" + long1)
#             print("LONG2-1:" + long2)
#         else:
#             if len(long2) > len(long1):
#                 long1 = long2
#                 print("X2:" + str(x))
#                 print("LONG1-2:" + long1)
#                 print("LONG2-2:" + long2)
#             long2 = ''
#     print("X3:" + str(x))
#     print("LONG1-3:" + long1)
#     print("LONG2-3:" + long2)
# =============================================================================

# =============================================================================
# s = 'azcbobobegghikl'
# 
# long1 = ''
# long2 = ''
# for x in range(len(s) + 1):
#     if x <= (len(s) - 2):
#         if s[x] <= s[x + 1]:
#             if long2 == '':
#                 long2 += s[x:x+2]
#             else:
#                 long2 += s[x+1]
#             if len(long2) > len(long1):
#                 long1 = long2
#             print("X1:" + str(x))
#             print("LONG1-1:" + long1)
#             print("LONG2-1:" + long2)
#         else:
#             long2 = ''
#             print("X2:" + str(x))
#             print("LONG1-2:" + long1)
#             print("LONG2-2:" + long2)
#     print("X3:" + str(x))
#     print("LONG1-3:" + long1)
#     print("LONG2-3:" + long2)
# 
# 
# print(long1)
# print(long2)
# =============================================================================


s = 'zyxwvutsrqponmlkjihgfedcba'

long1 = s[0]
long2 = ''
for x in range(len(s) + 1):
    if x <= (len(s) - 2):
        if s[x] <= s[x + 1]:
            if long2 == '':
                long2 += s[x:x+2]
            else:
                long2 += s[x+1]
            if len(long2) > len(long1):
                long1 = long2
        else:
            long2 = ''

print("Longest substring in alphabetical order is: " + long1)