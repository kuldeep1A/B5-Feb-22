# Improving the user experience
# Step 5
'''
from hangman_art import logo, stages
import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
# Testing code.


# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You'r already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word,print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
'''

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
