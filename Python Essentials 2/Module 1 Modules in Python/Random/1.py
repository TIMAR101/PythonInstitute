import random


dc = {}

dc.setdefault(0, 0)

dc.setdefault(1, 0)

for ___ in range(100000000):

    m = random.randint(0,1)

    dc[m] += 1

print(dc)
