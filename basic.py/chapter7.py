# CHAPTER - 7 LOOPS 


for i in range(1,6): # jahan tak hoga ussey count nhi krta
    print(i)

i = 0
while(i<9):
    print(i)
    i += 1 

i = 0 
while(i<5):
    print("harry")
    i += 1

l = [ "harry", "deekshant", "kunal", "shubham","shubhi"]
i = 0

while(i<len(l)):
    print(l[i])
    i+=1
for i in range(0,100, 4): # gap dene ke liye same as slicing (RANGE FUNCTION H 4)
    print(i)


# for loop with list
l = [1, 4 , 5, 6, 7, 45]
for i in l:
    print(i)


# for loop with tuples
t = (6,231,75,122)
for i in t:
    print(i)


# for loop with strings
s = "harry"
for i in s:
    print(i)


# for loop with else

l = [1, 7, 8] 
for item in l:
    print(item) 
else:
    print("done")
# this is printed when the loop exhausts!


#break, continue, pass

for i in range(100):
    if(i==34):
        break # exit the loop right now
    print(i)
for i in range(100):
    if(i==34):
        continue # skip this iteration
    print(i)

pass #( baad mein kaam karoge ) null statement, instructs to do nothing

for i in range(645):
    pass
i = 0 
while(i<45):
    print(i); i+=1


# problem -1 table likhne ka code

n = int(input("enter a number"))
for i in range(1,11):
    print(f"{n}*{i}= {n*i}")


# problem -2  s se start suru hone wale name phele bolo 

l = ["harry", "sohan", "sachin", "rahul"]
for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")


# problem -3 prob 1 ko while loop se karo

n = int(input("enter a number"))
i = 1
while(i<11):
    print(f"{n} * {i} = {n*i}")
    i += 1


# problem -4 prime number enter kiya ki nhi 

n = int(input("enter a number"))
for i in range(2, n):
    if(n%i)==0:
         print("given number is not prime")
         break
else:
     print("number is prime")


# problem -5  phele n natural number ka sum find krna h whike loop se 

n = int(input("enter a number"))
i = 0
sum = 0
while(i<=n):
    sum += i
    i+=1
print(sum)


# problem -6 factoral likhna h 

n = int(input("enter a number"))
product = 1
for i in range(1, n+1):
    product = product*i
print (f"the factorial of {product}")


# problem -7 star pattern bnao

n = int(input("enter a number"))
for i in range (1, n+1):
    print(" "* (n-i), end ="")
    print("*"* (2*i-1), end ="")
    print("")


# problem -8 wapis

n = int(input("enter a number"))
for i in range(1, n+1):
    print("*"* i, end= "")
    print("")


# problem -9 wapis 

n = int(input("enter a number"))
for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n, end="")
    else:
        print("*",end="")
        print(" " * (n-2),end="")
        print("*",end="")
    print("")


# problem -10 ulti table print karo

n = int(input("enter a number"))
for i in range(1,11):
    print(f"{n} *{11- i} = {n*(11-i)}")