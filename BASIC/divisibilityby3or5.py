def calculate_sum_of_multiples(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

def main():
    try:
        # Get user input
        N = int(input("Enter a natural number (10 <= N <= 1000): ").strip())

        # Check if input is within the valid range
        if 10 <= N <= 1000:
            total = calculate_sum_of_multiples(N)
            print("\n--- Result ---")
            print(f"Sum of all multiples of 3 or 5 below {N} is: {total}")
        else:
            print("Error: Input out of bounds. Please enter a number between 10 and 1000.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid natural number.")

# Execute the main function
if __name__ == "__main__":
    main()
