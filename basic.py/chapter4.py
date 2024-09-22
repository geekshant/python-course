#CHAPTER - 4 list  

friends = ["krishna", 43.2, 40, "sourav"]
print(friends[0])
friends[0] = "greapes"
print(friends[0])

# list are MUTABLE, means it can change unlike strings(IMMUTABLE)
#slicing bhi kar skte h same as strings 

friends.append("deekshant")
print(friends)

l1 = [1,34,232,17,9,786]
l1.sort()
l1.reverse()
l1.insert(4, 69) 
l1.pop(3)
l1.remove(1) #jo h wo likhna padega index kaam nhi karta idher 
print(l1)


# # tuples (IMMUTABLE) in python

a = (1,) # coma lagane padenge warna yeh int ki class mein aajayega 
print(type(a))


# tuples method 

a =  (45, 76, 89, "deekshant", False,)
print(a)
no = a.count(45)
print(no)
i = a.index(45)
print(i)


# problem -1 fruits name store in a list 

fruits = []
f1 = str(input("enter fruits name"))
fruits.append(f1)
f2 = str(input("enter fruits name"))
fruits.append(f2)
f3 = str(input("enter fruits name"))
fruits.append(f3)
f4 = str(input("enter fruits name"))
fruits.append(f4)
f5 = str(input("enter fruits name"))
fruits.append(f5)
f6 = str(input("enter fruits name"))
fruits.append(f6)
f7 = str(input("enter fruits name"))
fruits.append(f7)
print(fruits)


# problem -2 accept marks & display in sorted manner 

marks = []
s1 = int(input("enter your marks"))
marks.append(s1)
s2 = int(input("enter your marks"))
marks.append(s2)
s3 = int(input("enter your marks"))
marks.append(s3)
s4 = int(input("enter your marks"))
marks.append(s4)
s5 = int(input("enter your marks"))
marks.append(s5)
s6 = int(input("enter your marks"))
marks.append(s6)
marks.sort()
print(marks)


# problem -3 summing of 4 digits in list 

numbers = []
n1 = int(input("enter a number "))
n2 = int(input("enter a number "))
n3 = int(input("enter a number "))
n4 = int(input("enter a number "))
print(n1+n2+n3+n4)
                   
l = [2, 4, 5, 6]
print(sum(l))


# problem -4 count 0 

a = (7, 0, 8, 0, 0, 9)
no = a.count(0)
print(no)


# problem -5 check tuple cannot change in python

a = (23, "deekshant", 54)
a[1]= "haaty"
print (a) # tuples are IMMUTABLE