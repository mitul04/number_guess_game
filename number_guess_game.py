# This is a simple number guessing game where the user has to guess a randomly generated number within a specified range.
# The game continues until the user decides to stop playing.

import random, math

choice = "yes"

while choice == "yes":
    start, stop = input("Give me two numbers for the guessing range: ").split()

    try:
        start, stop = map(int, (start, stop))

    except ValueError:
        print("Both must be numbers for this to work. Try again!")
        continue

    if start > stop:
        start, stop = stop, start

    number = random.randint(start, stop)
    guesses = 0
    best = math.ceil(math.log2(stop - start + 1))
    print("Let's see in how many guesses you can guess this number")

    while True:
        guess = input(f"Guess {guesses + 1}: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        guesses += 1

        if guess == number:
            print(f"\nYou got it right in {guesses} moves")
            print(f"I expected your guess in {best} moves.")

            if guesses < best:
                print("You are a genius!")
            elif guesses <= best + 2:
                print("Impressive guesswork!")
            else:
                print("Aim for lower moves next time!")

            break

        elif guess > number:
            print("You are ahead of the number")

        else:
            print("You are behind the number")

    choice = input("\nPlay again? (yes/no) ").strip().lower()

    if choice not in {"yes", "no"}:
        print("Invalid choice. Exiting the game.")
        break

print("\nThanks for playing!")
