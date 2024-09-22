# CHAPTER - 6 CONDITIONAL EXPRESSION


a = int(input("enter your age"))
if(a>= 18):
    print("you are an adult")
elif(a<=0):
    print("invalid age")    
else:
    print("your are not an adult")

# multiple if 
# 
a = int(input("enter your age : "))

# if statement no: 1
if(a%2==0):
    print("a is even");

# if statement no: 2  

if(a>=18):
    print("you are above thee age of consent")
    print("good for you");
elif(a<0):
    print("invalid age");
else:
    print("you are below the age of consent");
print("end of program")


# problem -1 fiind greatest number entered by users

n1 = int(input("enter a number 1: "))
n2 = int(input("enter a number 2: "))
n3 = int(input("enter a number 3: "))
n4 = int(input("enter a number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print(n1," is greater in all numbers")
elif(n2>n1 and n2>n3 and n2>n4):
    print(n2," is greater in all numbers")
elif(n3>n1 and n3>n2 and n3>n4):
    print(n3," is greater in all numbers")
elif(n4>n2 and n4>n3 and n1<n4):
    print(n4," is greater in all numbers")
elif(n1==n2==n3==n4):
    print("all numbers are equal")
else:
    print("invalid condition")


# problem -2  fail or pass 40% total and 33% in each 3 sub otherwise failed, marks from user as input 

m1 = int(input("enter your marks of biology: "))
m2 = int(input("enter your mark of chemistry: "))
m3 = int(input("enter your mark of physics: "))

total_percentage = (m1 + m2 + m3 )/3

if(total_percentage>=40 and m1>33 and m2>33 and m3>33):
    print("you are passed: ",total_percentage)
else:
    print("you are failed bruh: ",total_percentage)


# problem -3 spam comment ko delte krne wala code

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is spam");
else:
    print("this comment is not spam")


# problem -4 check length of username

a = input("enter a username: ")

if(len(a)>=10):
    print("username is right: ", len(a))
else:
    print("invalid username: ", len(a))


# problem -5 find given name is in list or not 

l = "herry", "shubham", "deekshant","kunal"
name = input("enter your name")

if(name in l):
    print("name is present");
else:
    print("yuor name is not present in list")


# problem -6 grading krni h student ki 

marks = int(input("enter your number"))

if(marks>=90):
    print("excellent");
elif(marks>=80):
    print("A");
elif(marks>=70):
    print("B");
elif(marks>=60):
    print("C");
elif(marks>=50):
    print("D");
elif(marks<50):
    print("F");
else:
    print("padh liya kar bhai")


# problem -7 program likh ke bta harry ke baare m baat ho rhi h ki nhi 

post = input("write about someone")

if("harry".lower() in post.lower()):
    print("this post is talking about harry")
else:
    print("this post is not talking about harry ")