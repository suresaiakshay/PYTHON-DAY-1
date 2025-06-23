def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero."

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    print("\nCommand Line Calculator")
    print("-----------------------")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        choice = input("\nEnter operation (1/2/3/4/5 or +/-/*//): ").strip().lower()
        
        if choice in ('5', 'exit', 'quit'):
            print("Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4', '+', '-', '*', '/'):
            print("Invalid choice. Please try again.")
            continue
        
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        if choice in ('1', '+'):
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice in ('2', '-'):
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice in ('3', '*'):
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice in ('4', '/'):
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()