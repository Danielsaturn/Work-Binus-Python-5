def introduction():
    print("""---------------------
| DANIEL     SATRIA |
|       Cinere      |
---------------------""")

def addition(value1, value2):
    
    addre= value1 + value2
    
    print(addre)

introduction()
arithch = str(input("Enter Menu (+|-|/|*|%|stop): "))
value1 = float(input("Please enter the first value: "))
value2 = float(input("Please enter the second value: "))

if (arithch == "+"):
    
    addition(value1, value2)
