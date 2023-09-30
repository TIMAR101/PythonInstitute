from module import suml, prodl

zeroes = [i for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import sys

for p in sys.path:
  print(p)

print(type(sys.path))

