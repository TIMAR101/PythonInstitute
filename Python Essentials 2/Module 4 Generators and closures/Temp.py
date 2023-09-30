# def fun(n):
#     for i in range(n):
#         yield i
#
#
# for v in fun(5):
#     print(v)

for x in (el * 2 for el in range(5)):
    print(x, end='')
