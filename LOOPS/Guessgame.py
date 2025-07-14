# Set a secret number (the number your friend needs to guess)
secret_number = 42

# Start a while loop to repeatedly ask for guesses
while True:
    # Ask the user to guess a number
    guess = int(input("Guess the number to get the class notes: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You've guessed the correct number. Here's the class notes!")
        break  # Exit the loop since the correct guess was made
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
