# CHAPTER - 9 FILE I/O


'''
a = "a very long string with emails"
emails =[]
3 seconds
'''
# file write krna 

st = " deekshant you are idiot "
f = open("myfile.txt","w")
f.write (st)
f.close()

# file read krna 

a = "deekshant is a idiot"
f = open("myfile.txt")
f.read(f.close())

f = open("file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()

'''
r = read / default mode
w = write
a = append
+ = to update
rb = read in binary mode
rt = read in text mode / default mode

'''
f = open("file.txt")
print(f.read())
f.close()

'''the same can be written using (with statement) like this:'''

with open("file.txt")as f:
 print(f.read())

'''you dont have to explicitly close the file '''


# problem -1 file se txt read kro aur find karo ki wo twinkle word contain krti h ki nhi 

f = open("poem.txt")
c = f.read()
if("twinkle"):
    print("yes")
else:
    print("not present")
f.close()


# problem -2 game khilwana aur score dikhana aur high score ... agar high score toda toh wo bhi dikhana 

import random

def game():
    print("you are plaing game..")
    score = random.randint(0,6)
    '''fetch the high score'''
    with open("highscore.txt") as f:
        highscore= f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0          
        print(f"your score : {score}")
    if(score>highscore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))          
    return score
game()


# problem -3 2 se 20 ki table likho aur usse file m place/store krao

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"      
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)      
    for i in range(2,21):
        generateTable(i)


# problem -4 file ne bhut baar donkey naam contain kra replace krakr usko #### krna h 

word = "donkey"
with open("file.txt")as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("file.txt", "w") as f:
    content = f.write(contentNew)


# problem -5 chaute ko repeat kro aur censored words hatao.

words = ["donkey", "bad", "ganda"]

with open("file.txt")as f:
    content = f.read()
for word in words:content = content.replace(words, "#" * len(word))

with open("file.txt", "w") as f:
    content = f.write(content)


# problem -6 min log file and find whether it contains"python"

with open ("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("python is present")
else:
    print("no python is not present")
   
    
# problem - 7 line number find kro que 6 ka

with open ("log.txt") as f:
    line = f.readline()

line = 1 
for line in lines:
 if ("python" in line):
    print(f"python is present. line no: {line}")
 break
 line += 1 

else:
    print("no python is not present")


# problem -8 copy bnao file ki

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)


# problem -9 identical h ki nhi ?

with open("file1.txt") as f:
    content1 = f.read()
with open("file2.txt") as f:
    content2 = f.read()
if(content1 == content2):
    print("content is same")
else:
    print("nope, content not same")


# problem -10 wipe out file content 

with open ("this.file") as f:
    f.write("")


# problem -11 file rename kro

with open("this.txt") as f:
    content = f. read()
with open("rename.txt") as f:
    f.write(content)