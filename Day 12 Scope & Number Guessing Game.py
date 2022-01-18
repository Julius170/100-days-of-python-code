# SCOPES
import random

# MY SOLUTION (ALL BY ME... 😊)
# print("Welcome to the Number Guessing Game!")
# print("I am thinking of a number rbetween 1 to 100.")
# ANSWER = random.choice(range(1, 100))

# level = input("Choose a difficullty. Type 'easy' or 'hard': ")

# if level == "easy":
#     attempt = 10
#     print(f"You have {attempt} attemps to guess the number.")
# elif level == "hard":
#     attempt = 5
#     print(f"You have {attempt} attemps to guess the number.")
# else:
#     print("Invalid input")
# start = 0


# while attempt > start:
#     attempt -=1
#     guessed = int(input("Make your guess: "))
#     if guessed > ANSWER:
#         print("Too high.\n Guess again.")
#     elif guessed < ANSWER:
#         print("Too low.\n Guess again.")
#     elif guessed == ANSWER:
#         print("You Win.") 
#         attempt = 0
#     print(f"You have {attempt} attempts remaining to guess the number.")


# COURSES SOLUTION
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turn = 0


def check_answer(guess, answer, turn):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turn - 1
    elif guess < answer:
        print("Too low.")
        return turn - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Guessing Game.")
    print("I'm thinking of a between 1 and 100.")
    answer = randint(1, 100)

    turn = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turn} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

# FINITE
