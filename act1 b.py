import math

def display_menu():
    print("\n===============================")
    print("         Simple Calculator      ")
    print("===============================")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exit")
    print("===============================")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def main():
    print("Welcome to the Simple Calculator!")
    print("Let's do some math magic together!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '5':
            print("Thank you for using the Simple Calculator! Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "×"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "÷"

            print("\nANG SAGOT SA KATANUNGAN MO AY! ✨😆")
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid input! Please select a valid operation.")

if __name__ == "__main__":
    main()