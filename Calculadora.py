def calcular (num1, num2, operation):
    if operation == "+":
        print("Result: ", num1 + num2)
    elif operation == "-":
        print ("Result: ", num1 - num2)
    elif operation == "*":
        print ("Result: ", num1 * num2)
    elif operation == "/":
        print ("Result: ", num1 / num2)
    else:
        return ("Operation failed")
if __name__=="__main__":
    num1 = float(input("Enter number one: "))
    num2 = float(input("Enter number two: "))
    operation= input("Choose a operation (+,-,*,/): ")
    print("Result:", calcular(num1, num2, operation))