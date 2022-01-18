# HANGMAN PROJECT
# STILL HAVE TO  UNDERSTAND THIS

import random

word_list = ["baboon", "camel", "aardvark"]

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

lives = 6

display = []
dash = "_"
for keys in chosen_word:
    display += dash
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a word? ").lower()

    if guess in display:
        print(f"You've already guessed the word {guess}")
    for position in range(word_len):
        # print (position)    
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word,You lose a life")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

# print (word_len)


# FINITE
