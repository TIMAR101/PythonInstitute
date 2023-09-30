def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n

            # ttgtgtg
            yield n

fibs = list(fibonacci(10))
print(fibs)

fibs1 = [a for a in fibonacci(10)]
print(fibs1)

