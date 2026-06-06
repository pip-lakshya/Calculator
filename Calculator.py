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
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print("Addition =", result)
    elif(choice==2):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print("Subtraction =", result)
    elif(choice==3):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print("Multiplication =", result)
    elif(choice==4):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num2 != 0:
            result = num1 / num2
            print("Division =", result)
        else:
            print("Division by Zero is not allowed.")
    elif(choice==5):
        pass
    elif(choice==6):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 % num2
        print("Remainder =", result)
    elif(choice==7):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num2 != 0:
            print("Floor Division = ",num1 // num2)
        else:
            print("Division by Zero is not allowed.")
            
    elif(choice==8):
        num=int(input("Enter a number: "))
        print("The square root of ",num," is ",sqrt(num))
    elif(choice==9):
        print("Exiting the calculator")
        break
    else:
        print("Invalid choice")