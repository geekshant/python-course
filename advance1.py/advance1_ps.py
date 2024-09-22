# problem -1 write a program to open three files 1.txt, 2.txt, 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same 

'''try:
    with open("1.txt", "r") as f:
     print(f.read())
except Exception as e:
    print(e)

try:    
    with open("2.txt", "r") as f:
     print(f.read())
except Exception as e:
    print(e)

try:   
    with open("3.txt", "r") as f:
     print(f.read())
except Exception as e:
    print(e)

print("thank you")'''


# problem -2 write a program that prints third, fifth and seventh element from the list using enumerate function

'''l = [4, 5, 6, 85, 434, 34, 76, 0]

for i, item in enumerate(l):
    if i == 2 or i ==4 or i == 6:
     print(item)'''
     
# problem -3 write a list comprehension to print a list which contains the multiplication table of a user entered number.

'''n = int(input("enter a number: "))

l = [n*i for i in range(1,11)]

print(l)'''

# problem -4 write a program to display a/b where a and b are integers. if b==0, display infinite by handling 'ZeroDivisionError'

'''try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("infinite")'''
    

# problem -5 store the multiplication table generated in problem 3 in a file named table.txt

'''n = int(input("enter a number: "))

l = [n*i for i in range(1,11)]

with open("table.txt", "a") as f:
    f.write(f"table of {n}: {str(l)} \n ")'''