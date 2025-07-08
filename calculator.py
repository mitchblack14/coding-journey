import math

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Calculate x to the power of y"""
    return x ** y

def square_root(x):
    """Calculate square root"""
    if x < 0:
        return "Error: Cannot calculate square root of negative number!"
    return math.sqrt(x)

def percentage(x, y):
    """Calculate x% of y"""
    return (x / 100) * y

def calculator():
    """Main calculator function"""
    print("🔢 Simple Calculator")
    print("==================")
    
    while True:
        # Display menu
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Percentage (x% of y)")
        print("8. Exit")
        
        choice = input("\nEnter choice (1-8): ")
        
        if choice == '8':
            print("Thanks for using the calculator! 👋")
            break
        
        if choice in ['1', '2', '3', '4', '5', '7']:
            # These operations need two numbers
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                    print(f"\n{num1} + {num2} = {result}")
                
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(f"\n{num1} - {num2} = {result}")
                
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(f"\n{num1} × {num2} = {result}")
                
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
                
                elif choice == '5':
                    result = power(num1, num2)
                    print(f"\n{num1} ^ {num2} = {result}")
                
                elif choice == '7':
                    result = percentage(num1, num2)
                    print(f"\n{num1}% of {num2} = {result}")
                    
            except ValueError:
                print("❌ Error: Please enter valid numbers!")
        
        elif choice == '6':
            # Square root only needs one number
            try:
                num = float(input("Enter number: "))
                result = square_root(num)
                print(f"\n√{num} = {result}")
            except ValueError:
                print("❌ Error: Please enter a valid number!")
                
        else:
            print("❌ Invalid choice! Please select 1-8.")

# Run the calculator
if __name__ == "__main__":
    calculator()