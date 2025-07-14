def generate_pascals_triangle(n):
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        
        coef = 1  # First coefficient is always 1
        for j in range(i + 1):
            print(coef, end=" ")
            coef = coef * (i - j) // (j + 1)  # Calculate the next coefficient
        print()  # New line for the next row

def main():
    while True:
        try:
            # Prompt the user for input
            n = int(input("Enter a positive integer to generate Pascal's Triangle: "))
            if n > 0:
                break
            else:
                print("Error: Please enter a positive integer.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
    
    # Generate Pascal's Triangle
    generate_pascals_triangle(n)

if __name__ == "__main__":
    main()
