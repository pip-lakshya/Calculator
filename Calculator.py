import math
def sqrt(x):
    return math.sqrt(x)

while True:
    choice=int(input("""Enter a number to choose from 
        1. Addition 
        2. Subtraction
        3. Multiplication
        4. Division
        5. Power
        6. Modulus
        7. Floor division
        8. Sqrt
        9. Exit\n"""))
    if(choice==1):
        pass
    elif(choice==2):
        pass
    elif(choice==3):
        pass
    elif(choice==4):
        pass
    elif(choice==5):
        pass
    elif(choice==6):
        pass
    elif(choice==7):
        pass
    elif(choice==8):
        num=int(input("Enter a number: "))
        print("The square root of ",num," is ",sqrt(num))
    elif(choice==9):
        print("Exiting the calculator")
        break
    else:
        print("Invalid choice")