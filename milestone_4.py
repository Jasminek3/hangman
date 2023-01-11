#%%
import random 
word_list = ['mango','banana','apple','kiwi','strawberry']
letter_list = []

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_lives = num_lives
        self.list_of_guesses = letter_list
        self.num_letter = 26-(len(letter_list))

        print(f"Unique guesses left: {self.num_letter}")

    def check_guess(self, guess):
        guess = guess.lower
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
        else:
            print(f'Sorry, {guess} is not in the word. Try again')

    def ask_for_input(self):
        guess = input('Guess a Letter')
        while True:
            if guess.isalpha()!=True and len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)


# %%
