l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqlist = map(square, l)

print(list(sqlist))

# FILTER Example 

from functools import reduce

def even(n):
    if(n%2==0):
        return True
    return False
OnlyEven = filter(even,l)
print(list(OnlyEven))

# Reduce function example 

def sum(a, b):
    return a + b
mul = lambda x,y: x*y

print(reduce(mul,l))