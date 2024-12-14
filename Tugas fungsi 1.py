def introduction():
    print("""---------------------
| DANIEL     SATRIA |
|       Cinere      |
---------------------""")
#this definition is for introducing the creator of this code

def addition(value1 = 0, value2 = 0):
    
    addre= value1 + value2
    
    return addition
#this definition is for addition

def subtraction(value1 = 0, value2 = 0):
    
    addre= value1 - value2
    
    return subtraction
#this definition isfor subtraction

def division(value1 = 0, value2 = 0):
    
    addre= value1 / value2
    
    return division
#this definition is for division

def multiplication(value1 = 0, value2 = 0):
    
    addre= value1 * value2
    
    return multiplication
#this definition is for multiplication

def modulus(value1 = 0, value2 = 0):
    
    addre= value1 % value2
    
    return modulus
#this definition is for modulus

while (True):
    introduction()
    arithch = str(input("Enter Menu (+|-|/|*|%|stop): "))
    value1 = float(input("Please enter the first value: "))
    value2 = float(input("Please enter the second value: "))
    
    if (arithch == "+"):
        
        addition(value1, value2)
        print("the result of", value1, "+", value2, "is", addre)
        
    elif (arithch == "-"):
        
        subtraction(value1, value2)
        print("the result of", value1, "-", value2, "is", addre)
        
    elif (arithch == "/"):
        
        division(value1, value2)
        print("the result of", value1, "/", value2, "is", addre)
        
    elif (arithch == "*"):
        
        multiplication(value1, value2)
        print("the result of", value1, "*", value2, "is", addre)
        
    elif (arithch == "%"):
        
        modulus(value1, value2)
            print("the result of", value1, "%", value2, "is", addre)
        
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
