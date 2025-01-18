import time
import random


def error_check(x):
    try:
        x = int(x)
        return True

    except ValueError:
        return False


def game():
    game_answer = random.randint(1, 100)
    game_start_time = time.time()
    higher_statements = ["Nope, higher! ", "HIGHER ", "Too low... ", "Go higher! "]
    lower_statements = ["Lower!! ", "TOO HIGH! ", "Too big... ", "Go lower "]
    guess = input("What's your first guess? ")

    error_check(guess)

    while not error_check(guess):
        print("You need to enter a whole number!")
        guess = input("What's your first proper guess? ")

    guess = int(guess)

    while guess != game_answer:

        if guess < game_answer:
            print(random.choice(higher_statements))

        elif guess > game_answer:
            print(random.choice(lower_statements))

        guess = input("Next guess? ")

        while not error_check(guess):
            guess = input("I NEED A WHOLE NUMBER! ")

        guess = int(guess)

    finish_time = time.time() - game_start_time

    print(
        f"Good job! The answer was {game_answer}. You finished in {round(finish_time, 2)} seconds!"
    )
    print("Wanna play again?")
    time.sleep(0.8)

    again = input("Type 'Yes' to play again, or 'No' to exit. ")

    while again not in ["Yes", "yes", "No", "no"]:
        again = input("Invalid input. Please try again ")

    if again in ["Yes", "yes"]:
        time.sleep(1.2)
        game()

    else:
        print("Thanks for playing! See you later! ")
        return


def game_intro():

    print("Let's play a game!")
    time.sleep(1.1)
    print("I'm gonna think of a random number between 1 and 100.")
    time.sleep(1.1)
    print("Each guess you make, I'll tell you higher or lower")
    time.sleep(1.1)
    print("How fast can you win?")
    print("On 3..")
    time.sleep(1.1)
    print("2...")
    time.sleep(1.1)
    print("1...")
    time.sleep(1.1)
    game()


game_intro()
