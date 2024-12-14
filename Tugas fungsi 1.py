def introduction():
    print("""---------------------
| DANIEL     SATRIA |
|       Cinere      |
---------------------""")
#this definition is for introducing the creator of this code

def addition(value1 = 0, value2 = 0):
    
    addre= value1 + value2
    
    return addre
#this definition is for addition

def subtraction(value1 = 1, value2 = 1):
    
    addre= value1 - value2
    
    return addre
#this definition isfor subtraction

def division(value1 = 1, value2 = 1):
    
    addre= value1 / value2
    
    return addre
#this definition is for division

def multiplication(value1 = 1, value2 = 1):
    
    addre= value1 * value2
    
    return addre
#this definition is for multiplication

def modulus(value1 = 1, value2 = 1):
    
    addre= value1 % value2
    
    return addre
#this definition is for modulus

while (True):
    introduction()
    arithch = str(input("Enter Menu (+|-|/|*|%|stop): "))
    
    if (arithch == "stop"):#Put it here so when user type stop, it sdoes not pop up the value system
        
        break
    
    value1 = float(input("Please enter the first value: "))
    value2 = float(input("Please enter the second value: "))
    
    if (arithch == "+"):
        
        addre = addition(value1, value2)
        print("the result of", value1, "+", value2, "is", addre)
        
    elif (arithch == "-"):
        
        addre = subtraction(value1, value2)
        print("the result of", value1, "-", value2, "is", addre)
        
    elif (arithch == "/"):
        
        addre = division(value1, value2)
        print("the result of", value1, "/", value2, "is", addre)
        
    elif (arithch == "*"):
        
        addre = multiplication(value1, value2)
        print("the result of", value1, "*", value2, "is", addre)
        
    elif (arithch == "%"):
        
        addre = modulus(value1, value2)
        print("the result of", value1, "%", value2, "is", addre)
        
        
    else:
        
        print("PLEASE enter the correct arithmatic operator as shown in the menu!")
        
    
    continuing = input("Do you want to continue (type:'yes' or 'stop'): ") #We are using a while for looping
    
    if (continuing == "yes"):
        
        continue
    
    else:
        
        print("Force break due to not adding the correct word")
        break
