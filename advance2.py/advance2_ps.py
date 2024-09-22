# problem -1 create two virtual enviornments, install few packages in the first one. How do you create a similar enviornment in the second one ?

'''
 open command prompt 
 
 virtualenv env1
 virtualenv env2
 
 .\env1\scripts\activate.ps1
 pip install pandas
 pip install pyjokes

pip freeze > requirements.txt
deactivate env1

.\env2\scripts\activate.ps1
pip install -r requirements.txt
'''

# problem -2 write a program to input name, marks and phone no. of a student and format it using the format func like below: "the name of the student is deekshant, his marks is 72 and phone no. is 8574961253"

'''n = str(input("enter your name: "))
m = int(input("enter your marks: "))
pn = int(input("enter your phone number: "))

a = "the name of the student is {}, his marks is {} and phone number is {}".format(n,m,pn)
print(a)'''

# problem -3 a list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers 

'''table = [str(7*i) for i in range(1,11)]
t = "\n".join(table)
print(t)'''

# problem -4 write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if(n%5==0):
        return True
    return False
a = [1, 5, 65, 80, 73, 600]

f = list(filter(divisible5, a))

print(f)


# problem -5 write a program to find the maximum of the numbers in a list using the reduce fn.

from functools import reduce

l = [1, 5, 65, 80, 73, 600, 38, 198675, 83674,23865]

def greater(a,b):
    if(a>b):
        return a 
    return b
print(reduce(greater,l))


# problem -6 run pip freeze for the system intepreter. take teh contents and create a similar virtualenv

'''
pip freeze > requirements.txt
virtualenv en1
'''

# problem- 7 explore 'flask' module and create a web server using flask and pyhton

