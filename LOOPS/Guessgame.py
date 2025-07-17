import random

# Set the secret number
secret_number = 42  # You can use random.randint(1, 100) for variation

print("Welcome to the Guessing Game!")
print("You need to guess the secret number to unlock the class notes.")
print("Hint: It's between 1 and 100.")

attempts = 0  # Counting the number of tries

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts.")
            print("Here's the class notes. Use them wisely!")
            break
        elif abs(guess - secret_number) <= 3:
            print("Very close! You're just a few numbers away.")
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
