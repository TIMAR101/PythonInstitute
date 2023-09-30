def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

t = [x for x in powers_of_2(9)]
print(t)
v = list(powers_of_2(9))
print(v)

print(5 in powers_of_2(5))

