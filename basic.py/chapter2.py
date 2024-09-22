# CHAPTER -2 

a = 1
b = 3
print(a+b)

''' integer,boolean,none,floating point number,string - data types 
 operators - arthematic(+-*/), assignment(=,+=, -=), comaparison(==,>,>=,<=,<,!=), logical(and, or , not)'''


# type function
 
a = 1
t = type(a)
print(t)

a = "31.2"
b = float(a)
t = type(b)
print(t)

a = int ( input("enter number 1 : "))
b = int ( input("enter number 2 : "))

print ("sum is ", a+b)


#problem -1 addition 
a = 1 
b = 2 
print(a + b)


#problem -2 remainder 
a = 34
b = 4
print("remainder when a is divided by b is ", a%b) # modulo(% is for remainder)


#problem -3 check type ofvariable through input
a = input("enter something")
t = type(a)
print(t)   


#problem -4 comparison 

a = 34 
b = 80 
if(a>=b):{
    print("a is greater than b")
}
else:{
    print("a is smaller than b")
}


#problem -5 finding average 

a = int(input("enter a number "))
b = int(input("enter a number "))
print("the average of two number is ", (a+b)/2)


#problem -6 squaring 

a = int(input("enter a number "))
print(" the square of a number is ", a*a)  # or (**2 for square and **3 for cube, ^ not valid)