import random

choice = "yes"

while choice.lower() == "yes":
    start, stop = input("Give me a range of numbers: ").split()

    if start.isdigit() and stop.isdigit():
        start, stop = map(int, (start, stop))

    else:
        print("Both should be numbers.")
        quit()

    number = random.randint(start, stop)
    guesses = 0

    print("Let's see in how many guesses you can guess this number")

    while True:
        guesses += 1
        guess = input(f"Guess {guesses}: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)

        if guess == number:
            print("You got it right in", guesses, "guesses")
            break

        elif guess > number:
            print("You are ahead of the number")

        else:
            print("You are behind the number")

    choice = input("Play again? (yes/no) ")

else:
    print("Thanks for playing!")
    quit()
    