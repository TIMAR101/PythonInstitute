
l1 = [1,2,3,4,5]

m1 = map(lambda x: x*x, l1)

print(list(m1))

m2 = filter(lambda x: x % 2 == 0, l1)

print(list(m2))


# Recommended:
def f(x): return 3*x

print(f(3))


# Not recommended:
f = lambda x: 3*x

print(f(3))



print(list(map(lambda x: str(x), l1)))

print(l1)

print(list(filter(lambda x: x > 3, l1)))

#for bit in bits[-2::-1]:

print(l1[-2::-1])
