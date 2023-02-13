
import sys
print("Hello World, ACHIEVE YOUR GOALS !!!!")
# to pass arguments in the terminal, "python.exe filename.py arguments.
# python.exe Example1.py jk kl lm or python tab arguments
n=len(sys.argv)
print('Arguments:',sys.argv)                             
print('number of arguments',n)
if n>1:
    name =sys.argv[1]
    print('Arg 1',name) # 1 tab is equivalent to 4 spaces
#elif n<0:
#   pass
else:
    name=None
    print("pass arguments")
print("Argument lists")

#for loop
for arg in sys.argv:
    print('-',arg)
print("Last argument !",sys.argv[-1])

#Slicing of lists
drinks =sys.argv[2:]
for drink in drinks:
    print("I drink", drink)

#Slicing of lists
ville ='Toulouse'
print(ville)
print(ville[:3])
print(ville[-3:])

# while loop
i=10
while i>=0:
    print(i, end='\n')
    i-=1
print("Done")

#Operators
print("typecasting",int(11/3)) #type casting 
print("// division",11//3)

print("hello"*4 )
print("hello"+" "+"jo")

# logical operators
a,b=3,4
if a is b:   # (is and is not or == or !=)
    print(a,"equals",b)
else:
    print(a,"not equals",b)
    


drink_wanted ='thé'
found=False
for drink in drinks:
    if drink ==drink_wanted:
        found=True
        break
if found:
    print(" you can drink",drink_wanted)
else:
    print("sorry there is no",drink_wanted)


input =sys.argv[0:]
for j in input:
    match j:
        case "tea":
            print("you have choosen tea")
        case "juice":
            print("juiceddddsf")


"""
The sys argv list is a list that contains command line arguments in a python program.
 Whenever we run a python program from a command line interface, we can pass different arguments to the program. 
 The program stores all the arguments and the file name of the python file in the sys.argv list."""


