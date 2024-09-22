l =[1, 9, 7, 6, 5]

'''sqli =[]
for item in l:
    sqli.append(item*item)
    
print(sqli)'''

# list comprehension ke through

sqli = [i*i for i in l]

print(sqli)