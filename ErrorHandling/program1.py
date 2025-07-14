# Basic Python program with exception handling description 

try:
    # Taking two numbers as input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Trying to divide the numbers
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
    
except ZeroDivisionError:
    # Catching the division by zero error
    print("Error: Cannot divide by zero!")
    
except ValueError:
    # Catching invalid input errors (e.g., non-numeric input)
    print("Error: Please enter valid numbers!")

except Exception as e:
    # Catching any other general errors
    print(f"An error occurred: {e}")

