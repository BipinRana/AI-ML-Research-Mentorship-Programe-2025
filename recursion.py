#Recursion to find factorial
def factorial(x):
    return x*factorial(x-1) if x>0 else 1
print(factorial(5))

#Recursion to find nth fibonacci number
def recursion(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return recursion(x-1)+recursion(x-2)
print(recursion(5))

#Recursion to find exponential/power of a number
def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp-1)
print(power(9,3))