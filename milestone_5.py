
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
            for index, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed) 
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)      

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

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives==0:
            print("You lost!")
            break
        elif game.num_letters>0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(word_list)
                
# %%
