def count_down(n):
    # Validate input first
    if n < 0 or n > 60:
        print("Please enter seconds between 0 and 60.")
        return

    # Countdown loop
    for i in range(n, -1, -1):  # Start from n, go down to 0
        print(i)
        if i == 0:
            print("Time Up!")

            
Flag = False
while Flag == False:
    try:
        # Input from the user
        n = int(input("Enter seconds to countdown: "))
        count_down(n)
        Flag = True
    except ValueError:
        # Handle non-integer input
        print("Invalid input! Please enter a valid integer.")
        Flag = False