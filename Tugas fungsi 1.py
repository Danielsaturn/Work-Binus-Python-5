def introduction():
    print("""---------------------
| DANIEL     SATRIA |
|       Cinere      |
---------------------""")
#this definition is for introducing the creator of this code

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

def multiplication(value1, value2):
    
    addre= value1 * value2
    
    print(addre)
#this definition is for multiplication

while (True):
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
        
    elif (arithch == "*"):
        
        multiplication(value1, value2)
        
    else:
        
        print("PLEASE enter the correct arithmatic operator as shown in the menu!")
    
    continuing = input("Do you want to continue (type:'yes' or 'stop'): ") #We are using a while for looping
    
    if (continuing == "yes"):
        
        continue
    
    elif (continuing == "stop"):
        
        break
    
    else:
        
        print("This has been forced break due to incorrect input")
        break
