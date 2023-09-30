def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

nums = [-1,2,1,-4]
target = 1

a = min([(x, abs(target - x)) for x in nums], key=lambda a: a[1])[0]

print(a)


b = min([y for y in nums], key= lambda z: abs(z))

print(b)
