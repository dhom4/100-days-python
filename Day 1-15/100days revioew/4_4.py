from stages import stages
import random

word_list = ["apple", "banana", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


lives = 6

game_over = False
correct_letters = ""

while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO: Change the for loop so that you keep the previous correct letters in display.
    display = ""
    
    for letter in chosen_word:
        if letter == guess :
            display += letter
            correct_letters+= letter # this will acomlate the correct letters
        elif letter in correct_letters: # if the letter is not in equal to the guess, but the letter in the correct letters print it to the display as well.
            display += letter
        else:
            display += "_"
            
    print(display)

    """this was hard to postioin the right placn"""
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lost!")

    if "_" not in display:
        game_over = True
        print("you win")
        
    print(stages[lives])
