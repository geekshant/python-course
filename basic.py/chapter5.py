# CHAPTER - 5 SETS & DICTIONARY 

marks = {
    "harry" : 100,
    "deekshant" : 98,
    "rohan" : 23
}
print(marks, type(marks))

print(marks["harry"])


# dictionary methods 

print(marks.items())
print(marks.keys())
print(marks.values()) 
marks.update({"harry":99}) # add bhi kr skte h isi se  
print( marks)

print(marks.get("harry")) # yeh none deta h galat hone per
print(marks["harry"]) # yeh error deta h 


# # sets ( unordered, unidexed, cant change items in set, cant contain duplicate values )

d = {} # empty dictionary
s = {1, 2, 35 } # set with digits
e = set() # empty set 

s = { 1,2,3,4,76,94,28,"deekshant"}
s1 = {5, 4, 3, 2, 1}
s.add(688)
s.remove(1)
s.clear() # clears the set 
print(s.union(s1))
print(s, type(s))
print(s.intersection(s1))
 

# problem -1 make dict with hindi enfg word meaning 

meaning = {
    "deekshant" : "king",
    "cat" : "billi"
}
word = input("enter the word : ")
print(meaning[word], type(meaning))


# problem -2  user se number lo aur unique number ko ek baar dikhao 

s = set()
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
n = int(input("enter a number"))
s.add(n)
print(s)


# problem -3 set with 18(int) & 18(str) 

s = set()
s.add(18)
s.add("18")
print(s)


# problem -4 length nikalni h 

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s,len(s))


# problem -5 type finder

s = {}
print(type(s))


# problem -6 empty dict bnake 4 lang add krke dikha value keys ke sath

d = {}

name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})

print(d)


# problem -7 2 dost ke naam same hue toh kya hoga (kuch nhi hoga bs update wala syntax update krta jata h toh last lang daali h wohi show hogi, values same ho sakti hai )

d = {}

name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
d.update({name:lang})

print(d)


# problem -8 value change kar skta h ? = ( nahi kar skte h pheli baat list nhi rkh skte set mein, dusri baat set indexation nhi hota toh change kese karoge )

s = {8, 7, 12, "harry", [1,2]}
s.update({"harry":"deekshant"})
print(s)