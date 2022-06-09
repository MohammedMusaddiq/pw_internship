"""
2)
Write a txt file which has a word in each line like:
Hands
Legs
India
Crow
Rain
...
Write a python code to read the file and store the words in the list

Write a function to guess a word randomly from the list.

Now, write a function which asks user to guess the chosen word letter by letter.
Show "incorrect" message to the wrong guessed letter.
Display  letters in the clue word that were guessed correctly.

Let say word is EVAPORATE

# >>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
Incorrect!
You left with 5 chances to guess.

# >>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on.

1)Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
3)When the player wins or loses, let them start a new game.
"""

import random

with open('sample.txt', 'r') as f:
    content = f.read()
    sample_list = content.split()
    f.close()
print(sample_list)


def random_word_f(sample):
    return random.choice(sample)


def start_game():
    random_word = random_word_f(sample_list)
    guess_limit = 6
    guessed_letters = ''
    print('the random word is: ', random_word)
    print()
    print('>>> Welcome to Hangman!')
    print('_ _ _ _ _ _ _ _ _')
    print()
    while guess_limit > 0:
        guessed_letter = input(">>> Guess your letter: ")
        print()
        if guessed_letter in random_word:
            print(f"the Guessed letter '{guessed_letter}' is in random word")
        else:
            guess_limit -= 1
            print(f"incorrect, the letter '{guessed_letter}' is not in random word.")
            print(f'You left with {guess_limit} chances to guess.')
        print()
        guessed_letters = guessed_letters + guessed_letter
        lost_count = 0
        for i in random_word:
            if i in guessed_letters:
                print(f"{i}", end="")
            else:
                print('_', end="")
                lost_count += 1
        if lost_count == 0:
            print()
            print('You won!')
            print()
            replay = input('Do you want to play again? (y/n) ')
            if replay == 'y':
                start_game()
            break
    else:
        print()
        print('You lost!')
        print()
        replay = input('Do you want to play again? (y/n) ')
        if replay == 'y':
            start_game()


start_game()
