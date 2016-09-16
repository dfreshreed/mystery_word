import random
import sys
from string import ascii_lowercase
with open("/usr/share/dict/words") as lines:
    lines = lines.readlines()
comp_word = random.choice(lines).lower().replace("\n", "")
# print(comp_word)
#  At the start of the game, let the user know how many letters the computer's word contains.
comp_letters = len(comp_word)
# print(comp_letters)
# Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. Assume the user will only submit one letter
good_guesses = []
bad_guesses = []
letter_list = 0
# print(comp_word)
print("Welcome to Mystery Word! You have 8 chances to guess my word! My word has {} letters in it".format(len(comp_word)))

blank_word = list("_" * comp_letters)
unused_words = list(ascii_lowercase)
# Let the user know if their guess appears in the computer's word
# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
# If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.
# print(comp_word)
while letter_list < 8:
    guess = input("Guess a letter: ").lower()
    if guess in comp_word:
        if guess in good_guesses:
            print("You've already guessed that letter! Please try again!")
        good_guesses.append(guess)
        for current_location, current_letter in enumerate(comp_word):
            if guess == current_letter:
                blank_word[current_location] = guess
        print("That guess is in the computer word! You have {}/8 guesses".format(letter_list))
        print(*blank_word)
        if guess in unused_words:
            unused_words.remove(guess)
        print(*unused_words)
        #print(list(comp_word), blank_word, "DANIELLE!!!!")
        # print(good_guesses)
        if blank_word == list(comp_word):
            print ("You win!")
            sys.exit()
    elif guess in bad_guesses:
        print("you already guessed that letter")

    else:
        bad_guesses.append(guess)
        letter_list += 1
        print("That guess is not in the computer's word! You have {}/8 guesses".format(letter_list))

if letter_list == 8:
    print("Game Over! Thanks for playing! You had {} wrong guesses. My word was {}.".format(letter_list, comp_word))




# Display the partially guessed word, as well as letters that have not been guessed.

# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess

# The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.
