from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

# for child in filter(None, [node.left, node.right]):
#                 child.val += node.val * 2
#                 dfs(child)



print(list(filter(None, [0,1,2,3, None, 4, 5, 0, 99])))
