def fun(n):
    for i in range(n):
        yield i


print(fun(5))

for i in fun(5):
    print(i)

gen1 = fun(7)

print(gen1)
list1 = list(gen1)
print(list1)


