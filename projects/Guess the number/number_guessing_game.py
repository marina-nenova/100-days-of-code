from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(answer, guess, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    elif guess < answer:
        print("Too low")
        return turns - 1
    elif guess > answer:
        print("Too high")
        return turns - 1


def set_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        return EASY_LEVEL_TURNS
    elif choice == "hard":
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(answer, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")


game()
