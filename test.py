a = set([1,2,3,4,5])
print(a.pop())


def outer_func(x):
    print("x=",x)
    def inner_func(y):
        print("y=",y)  
        return y
    return inner_func

a = outer_func(11)
print(a)

#Remember
#SOLID principle
#PEP 8 guidelines for python