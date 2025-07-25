import random
print("Welcome Hangman game!!!")

words = ["apple", "oragne", "cherry"]

chosen_word = random.choice(words)
print(chosen_word)

placeholder = ""
length_placholder = len(chosen_word)

for position in range(length_placholder):
    placeholder += "_"
print(f"{placeholder} \n")

guess = input("guss a letter: ").lower()

display = ""

for ch in chosen_word:
    if guess == ch:
        display += ch
    else:
        display += "_"

print(display)