# INHERITANCE 

# class employee:
#     company = "Amazon"
#     name = "default name"
#     def show(self):
#         print(f"the name is {self.name} and the company is {self.company}")
        
'''class programmer:
    company = "microsoft"
    def show(self):
         print(f"the name is {self.name} and the salary is {self.salary}")
         
    def show_language(self):
         print(f"the name is {self.name} and the salary is {self.salary}")'''
         
'''class coder:
    language = "pyhton"
    def printlanguages(self):
        print(f"the language is {self.language}")
        
         
class programmer(employee,coder):
    company = "microsoft"
    def showlanguages(self):
         print(f"the name of the company is {self.company} and the programming language is {self.language}")
         
a = employee()
b = programmer()

b.show()
b.printlanguages()
b.showlanguages()'''

# print(a.company, b.company)


'''class employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"the class attribute is {cls.a}")
        
    @property
    def name(self):
        return(f"{self.fname} {self.lname}")

    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a = 45

e.name = "deekshant sharma"

print(e.fname, e.lname)

e.show()'''


# OPERATOR OVERLOAD

'''class number:
    def __init__(self,n) -> None:
        self.n = n 
        
    def __add__(self, num):
        return self.n + num.n
    
n = number(1)
m = number(2)

print(n+m)'''

# problem -1 create a class (2-d vector) and use it to create another class representing 3-d vector

'''class twoDvector:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")
        
class threeDvector(twoDvector):
    def __init__(self, i, j, k) -> None:
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k ")
        
a =  twoDvector(1, 2)
a.show()
b =  threeDvector(5, 2, 3)
b.show()'''

# problem -2 create a class "pets" from a class 'animals' and futher create a class 'dog' from 'pets'. add a method 'bark' to class 'dog'

'''class Animals:
    pass

class Pets(Animals):
    pass
    
class Dogs(Pets):
    @staticmethod
    def bark() -> None:
         print(f"bow bow")
    
d = Dogs()
d.bark()'''

# problem -3 create a class 'Employee' and add salary and increment properties to it. write a method 'Salary afterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary. t

'''class Employee:
    salary = 234
    increment = 20
    i = increment/100
    @property
    def salaryafterIncrement(self):
        return (f"{self.salary + self.salary * self.i}")
    
    @salaryafterIncrement.setter
    def salaryafterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100
        
e = Employee()
print(e.salaryafterIncrement)
e.salaryafterIncrement = 280.8
print(e.increment)'''


# problem -4 write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds multiple them.

'''class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        image_part = self.r * c2.i - self.i * c2.r
        return complex(real_part, image_part)
    
    def __str__(self) -> str:
        return f"{self.r + self.i}i"

c1 = complex(1, 2)
c2 = complex(3, 4)
print(c1 + c2)
print(c1 * c2)'''

# problem -5 write a class vector representing a vector of n dimensions. overload the + and * operator which calculates the sum and the dot(.) product of them.

'''class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
        
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y+ self.z * other.z
        return result
    
    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})"
    
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)'''

# problem -6 write a __str__() method to print the vector as follows: 7i + 8j +10k 

'''class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
        
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y+ self.z * other.z
        return result
    
    def __str__(self):
        return f"vector({self.x}i + {self.y}j + {self.z}k)"
    
v1 = vector(1, 2, 3)
v2 = vector(4, 5, 6)
v3 = vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)'''

# problem -7 override the __len__() method on vector of problem 5 to display the dimension of the vector

'''class vector:
    def __init__(self, l):
        self. l = l
        
    def __len__(self):
        return len(self.l)
    
v1 = vector([1, 2, 3])
print(len(v1))'''