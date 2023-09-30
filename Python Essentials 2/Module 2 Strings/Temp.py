# # Demonstrating the ord() function.
#
# char_1 = 'a'
# char_2 = ' '  # space
#
# char_3 = 'ё'
#
# print(ord(char_1))
# print(ord(char_2))
# print(ord(char_3))
#
# for item in range(3000, 5000):
#     print(chr(item))


l1 = [[2, [5]]]

print(l1)

print(l1[0])



l1.append([3, [10]])

print(l1)



l1.append([l1[-1][0]+5, l1[-1][1] + [7]])

for item in l1:

    print(item)

print(l1)
