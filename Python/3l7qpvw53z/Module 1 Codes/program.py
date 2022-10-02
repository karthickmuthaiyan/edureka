print("Hello World")
print("Welcome to Edureka!!!")
fobj=open("program.py")
line=fobj.readline()
while line:
    print(line,end="")
    line=fobj.readline()
    ctr+=1

fobj.close()