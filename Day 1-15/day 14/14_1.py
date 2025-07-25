import random
import art
from game_data import data


def which_bigger(guess,x,y, x_name, y_name):
    if guess == 'a':
        if x > y:
            print("correct!")
            print(f"{x_name} is greater")
            print(f"{x_name}:{x}M , {y_name}:{y}M")
        elif x < y:
            print("incorrect!")
            print(f"{y_name} is greater")
            print(f"{x_name}:{x}M , {y_name}:{y}M")
    elif guess == 'b':
        if x > y:
            print("incorrect!")
            print(f"{x_name} is greater")
            print(f"{x_name}:{x}M , {y_name}:{y}M")
        elif x < y:
            print("correct!")
            print(f"{y_name} is greater")
            print(f"{x_name}:{x}M , {y_name}:{y}M")



def print_A(x):
    A_name = data[x]["name"]
    A_desc = data[x]["description"]
    A_country = data[x]["country"]
    print(f"Compare A: {A_name}, {A_desc}, from {A_country}.")


def print_B(y):
    B_name = data[y]["name"]
    B_desc = data[y]["description"]
    B_country = data[y]["country"]
    print(f"Compare B: {B_name}, {B_desc}, from {B_country}.")


def game():
    # Create random numbers to use later to access dict
    y = random.randint(0, 30)
    x = random.randint(0, 30)

    A_name = data[x]["name"]
    B_name = data[y]["name"]
    A_follower = data[x]["follower_count"]
    B_follower = data[y]["follower_count"]

    # print a and b in the correct format
    print(art.logo)
    print_A(x)
    print(art.vs)
    print_B(y)
    print(" "*2)

    guess = input("Who has more followers? type 'A' or 'B' : ").lower()

    which_bigger(guess,A_follower,B_follower, A_name, B_name)
    print(" "*2)

game()