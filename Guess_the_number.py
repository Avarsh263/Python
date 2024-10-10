import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to Guess the Number! I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while True:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
