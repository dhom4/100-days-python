import random
print("Welcome Hangman game!!!")

# TODO: chose random word and print
words = ["apple", "oragne", "cherry"]
chosen_word = random.choice(words)
print(chosen_word)

# TODO: have palceholder and print it 
placeholder = ""
length_placholder = len(chosen_word)
for position in range(length_placholder):
    placeholder += "_"
print(f"{placeholder} \n")


# TODO-4: make global correct letters ccollecter
#  mkae sure that you store the correct letters outside and you can use them to compare the set inside the loop.
correct_letters = ""

# TODO-1: make loop for the game until all placeholders is full
game_over = False
while not game_over:
    guess = input("guss a letter: ").lower()
    
    display = ""
    
    # TODO-3: check if the guss is in letters
    """ This code was hard for me to understand at first,
    but, it works as follow:
        - the loop checks every and each letter in the word induvidally 
        - check if the letter match the guss
        - if not, check if the letter is in the part of the correct letters i've typed
        - if not nighter of them and put '-'
    """
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters += letter 
        elif letter in correct_letters: # if the courrent iterate letter is in the correct letters set outside the loop, than print it.
            display += letter
        else:
            display+= "_"

    print(display)

    # TODO-2: turn off the loop (:
    if not '_' in display:
        print("you won!")
        game_over = True
    else:
        print("you lost!")
   