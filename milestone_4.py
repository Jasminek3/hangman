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

myInstance = Hangman(word_list)
print(len(myInstance.word))
print(len(myInstance.word_guessed))

