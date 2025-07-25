import random

EASY_LEVEL = 10
HARD_LEVEL = 5


# Function to check users' guess against actual answer
def check_answer(user_guss, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guss > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guss < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("logo")
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pass, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempt remaining to guess the number.")  

    # Repeat the guessing functionality if they get it wrong.
    guss = 0
    while guss != answer:
        guss = int(input("make a guss: "))
        turns = check_answer(guss, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guss != answer:
            print("Guess again.")


game()