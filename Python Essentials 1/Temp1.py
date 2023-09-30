my_list =  [x * x for x in range(5)]

#this is very importanttgtg
def fun(lst):

    del lst[lst[2]]
    return lst


print(fun(my_list))

