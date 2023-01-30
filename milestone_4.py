
#%%
import random 
word_list = ['mango','banana','apple','kiwi','strawberry']

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set(list(self.word)))
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.") 

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter')
            if guess.isalpha()==False & len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break
            self.list_of_guesses.append(guess)
        
myInstance = Hangman(word_list)
print(myInstance.word)
print(len(myInstance.word_guessed))
myInstance.ask_for_input()
# %%
