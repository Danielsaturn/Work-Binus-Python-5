def introduction():
    print("""---------------------
| DANIEL     SATRIA |
|       Cinere      |
---------------------""")
#this definition is for introducinfg the creator of this code

def addition(value1, value2):
    
    addre= value1 + value2
    
    print(addre)
#this definition is for addition

def subtraction(value1, value2):
    
    addre= value1 - value2
    
    print(addre)
#this definition isfor subtraction

def division(value1, value2):
    
    addre= value1 / value2
    
    print(addre)
#this definition is for division

introduction()
arithch = str(input("Enter Menu (+|-|/|*|%|stop): "))
value1 = float(input("Please enter the first value: "))
value2 = float(input("Please enter the second value: "))

if (arithch == "+"):
    
    addition(value1, value2)
    
elif (arithch == "-"):
    
    subtraction(value1, value2)
    
elif (arithch == "/"):
    
    division(value1, value2)
    
