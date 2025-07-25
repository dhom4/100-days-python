import random
print("Welcome Hangman game!!!")

words = ["apple", "oragne", "cherry"]

chosen_word = random.choice(words)
print(chosen_word)

guess = input("guss a letter: ").lower()
print()
for ch in chosen_word:
    if guess == ch:
        print("right")
    else:
        print("worng")