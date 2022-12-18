
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: - Import the stages from hangman_art.py and make this error go away.
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
import random
from hangman_words import word_list
from hangman_art import logo, stages

chose_word = random.choice(word_list)
print(logo)
word_length = len(chose_word)
print(chose_word)

display = []
for _ in range(word_length):
    display += "_"


end_of_game = True
level = 6

while end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You'r already guess guessed {guess}")

    for position in range(word_length):
        letter = chose_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chose_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        level -= 1
        if level == 0:
            print("You lose!")
            end_of_game = False

    print(' '.join(display))
    if "_" not in display:
        end_of_game = False
        print("You win.")

    print(stages[level])
