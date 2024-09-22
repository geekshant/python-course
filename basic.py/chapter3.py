# CHAPTER - 3 


# string slicing 

name = "harry"
nameshort = name[0:3] # starts from index 0 all the way to 3 ( excluding 3)
print(nameshort) 
print(name[1:3])
print(name[-4:-1])
print(name[1:4])
print(name[0:4])
print(name[1:5])


# #string functions 

name = "harry"
print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())

a = " harry is good boy\n but not a \'bad\' boy"
print(a)


#problem -1 use input 

name = input("enter your name : ")
print(f"good afternoon {name}")


#problem -2 fill in letter template 

letter = '''dear <|name|>,
you are selected! 
<|date|>'''  
print(letter.replace("<|name|>", "deekshant").replace("<|date|>","5 july 2027"))   
# .replace ki chaining ho jati h jese uper ki hai 


#problem -3 detect double space in string

name = "harry is a good  boy and"
print(name.find("  "))


#problem -4 replace krdo double space ab 

print(name.replace("  "," "))

'''strings are IMMUTABLE which means jo pichla name h wo change nhi hua h balki naya name print hua h agar name print kroge toh double space wala hi naam print hoga'''


#problem -5 escape sequence characters

letter = "dear deekshant,\nthis python course is easy.\nthanks!" 
print(letter)