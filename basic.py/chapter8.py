# CHAPTER - 8 FUNCTION AND RECURSION


# function defination

def avg():
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    average = (a + b + c)/3
    print(average)
avg() # function call


def goodDay():
    a = input("enter your name")
    print(f"good morning {a}")
goodDay()

# function with args

def goodDay(name, ending):
    print("good day, "+ name + ending)
    return "done"
goodDay("deekshant", " thank you")

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)
n = int(input("enter a number"))
print(f"the factorial of this number is: {factorial(n)}")


# problem -1 function to find the greatest of three numbers 

def great():
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
greatest = great()
print(f"the greater number is: {greatest}")


# problem -2 function to convert celcius to fahernheit

def conv():
    c = int(input("enter the temp in celcius"))
    return(c*9/5) + 32
convert = conv()
print(convert)


# problem -3 python ka print() func ko end mein new line print krne se kese rokoge = (end = "")

print("a")
print("b")
print("c", end = "")
print("d", end = "")


# problem -4 first n natural number ka addition

def sum_of_natural_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Enter a number: "))
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers(n)}")


# problem -5 print a pattern 

def pattern(n):
    if n==0:
        return
    print("*"*n)
    print(n-1)

pattern(3)


# problem -6 inches to cm 

def conv():
    n = int(input("enter a numbrer"))
    return n*2.54
convert = conv()
print(convert)


# pronblem -7 write a pyhton func to remove a given word from a list ad strip it at the same time 

def rem(l, word):
    n = []
    for item in l:
       if not(item == word):
           n.append(item.strip(word))
    return n
l = ["harry", "rohan", "shubham", "an"]
print(rem(l, "an"))


# problem -8  table likhni h 

def table():
    n = int(input("enter a number"))
    for i in range (1, 11):
       print(f"{n} X {i} = {n*i}")
multi = table()
print(multi)