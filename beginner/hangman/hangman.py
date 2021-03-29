# 1. import the require files
import random

from hangman_words import word_list
from hangman_art import stages, logo

# 2. create a require variables for hangman game
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# 3. create a blank for the number of
display = []
for _ in range(word_length):
    display += "_"

print(display)

# 4. get the input and run the program
while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"You have already guess {guess_letter}")

    # check for guess_word
    for index in range(word_length):
        letter = chosen_word[index]

        if guess_letter == letter:
            display[index] = letter

    # check if user is wrong
    if guess_letter not in chosen_word:
        print(f"You've guessed {guess_letter}, that is not in word. You lose a life.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lose.")

    # show the display
    print(f"{' '.join(display)}")

    # check if user answer all the letter
    if "_" not in display:
        end_of_game = True
        print("You win")

    # print the art
    print(stages[lives])

# 5. print the correct word
print(f"Correct word: {chosen_word}")