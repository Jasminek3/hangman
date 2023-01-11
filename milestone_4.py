import random 
word_list = ['mango','banana','apple','kiwi','strawberry']
letter_list = []

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_lives = num_lives
        self.list_of_guesses = print(letter_list)
        self.num_letter = 26-(len(letter_list))