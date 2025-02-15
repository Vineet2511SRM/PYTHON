def main():
    while True:
        try:
            # Get a list of integers from the user
            user_input = input("Enter a list of integers separated by spaces: ")
            numbers = list(map(int, user_input.split()))
            
            # Display the list
            print(f"\nYour list: {numbers}")
            
            while True:
                try:
                    # Ask for a number to find
                    search_num = int(input("Enter a number to find its index/indices: "))
                    
                    # Find all indices of the number
                    indices = [i for i, num in enumerate(numbers) if num == search_num]
                    
                    if indices:
                        print(f"\n✅ The number {search_num} is present at indices: {indices}")
                    else:
                        print(f"\n🚫 The number {search_num} is not present in the list.")
                    
                    return  # Exit the program after valid input and output
                except ValueError:
                    print("\n🚫 Invalid input! Please enter a valid integer.")
        except ValueError:
            print("\n🚫 Invalid input! Please enter a list of integers separated by spaces.")

if __name__ == "__main__":
    main()
