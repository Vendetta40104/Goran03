def calculator():
    while True:

        print("Simple Calculcator")
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        operation = input("Choose an operation (+, -, /, *): ")

        if operation == "+":
            print("Result:", num1 + num2)
        elif operation == "-":
            print("Result:", num1 - num2)
        elif operation == "*":
            print("Result:", num1 * num2)
        elif operation == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("can't divide by zero.")
        else:
           print("Invalid operation!")
           
        again = input("Do you want to calculate again (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

calculator()