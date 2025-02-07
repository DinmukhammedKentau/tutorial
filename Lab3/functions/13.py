import random


def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)

    # Greet the player
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    # Initialize the number of guesses
    guesses_taken = 0

    while True:
        # Ask for a guess from the player
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        # Check if the guess is too low, too high, or correct
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


# Run the game
guess_the_number()
