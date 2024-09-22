a = 89
def func():
    global a # it changes global var which is 89 in this case
    a = 4
    print(a)
    
func()
print(a)