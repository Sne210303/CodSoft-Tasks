def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    
    choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")

   
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        return

    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))


        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"

       
        print(f"{operation} of {num1} and {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")


calculator()