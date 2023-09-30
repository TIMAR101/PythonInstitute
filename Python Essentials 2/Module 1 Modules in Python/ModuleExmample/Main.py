
from sys import path

path.append('/Python Essentials 2/Module 1 Modules in Python/ModuleExmample/Modules/')


import Module
print(Module.__counter)

my_ls = [1, 2, 3, 4, 5]

print(Module.suml(my_ls))
print(Module.suml(my_ls))

print(Module.__counter)

import sys

for p in sys.path:
    print(p)


