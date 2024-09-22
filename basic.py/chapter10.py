''' CHAPTER - 10 OBJECT ORIENTED PROGRAMMING '''

# CLASS - blueprint to create an object

'''class employee:
    lang = "py"
    salary = 2500000

harry = employee()
harry.name = "harry"
print(harry.name, harry.salary, harry.lang)

rohan = employee()
rohan.name = "rohan"
print(rohan.name, rohan.lang, rohan.salary)'''

# here name is object attribute and salary and lang are class attributes as they directly belong to the class 

# instance vs class attributes - instance attributes takes over

'''class employee:
    lang = "py"
    salary = 2500000
    
    # self dena padta h warna error aata h
    def getInfo(self):
        print(f"the language is {self.lang}, the salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")

harry = employee()
harry.name = "harry"
harry.lang = "java"
print(harry.name, harry.salary, harry.lang)
harry.getInfo()'''

'''CONSTRUCTOR'''

'''def __init__(self):''' # dunder method which is automatically called
'''print("i am creating an object")'''
    
    
# problem -1 class programmer bnao aur info store krao 

'''class programmer:
    comapny = "microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode'''
    
'''p = programmer("harry", 1200000, 475001)
print(p.name, p.salary, p.pincode, p.comapny)
r = programmer("rohan", 1800000, 375201)
print(r.name, r.salary, r.pincode, r.comapny)'''

# problem -2 calculator naam ki class to find square, cube, square root of no.

'''class calc:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"square is {self.n*self.n}")
    def square(self):
        print(f"cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"square root is {self.n**1/2}")
    
a = calc(8)
a.square()  '''

# problem -3  class atrri a usse ob bnao set "a" dir using ob.a = o kya class attri change hua 

'''class demo:
    a = 4 
     
o = demo()

print(o.a) #print class attri cause instance attri absent 

o.a =0 # instance attri set kia 

print(o.a) # instance attri presnet h toh wohi print hua '''

# problem -4 2 prob mein static method daalo

'''class calc:
    def __init__(self, n):
        self.n = n
    @staticmethod # no self used 
    def hello():
        print("hello user")
    def square(self):
        print(f"square is {self.n*self.n}")
    def square(self):
        print(f"cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"square root is {self.n**1/2}")
    
a = calc(8)
a.hello()
a.square()'''

# problem -5 class train book tickets, get status(no. of seats) and other info 

'''from random import randint
class train:
    def __init__(self, trainno) -> None:
        self.trainno = trainno
    def book(self, fro, to):
        print(f"ticket is booked no. {self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"train no. {self.trainno} is running succesfully")
    def getfacetime(self, fro, to):
         print(f"ticket face time in train no. {self.trainno} from {fro} to {to} is {randint(1,9)}")
a = train(54268)
a.book("rampur", "delhi")
a.getstatus()
a.getfacetime("rampur", "delhi")'''

# problem -6 perimeter change kr skte bo inside the class 

'''yes we can, but readability kharab hogi'''