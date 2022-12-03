# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

MILESTONE 2
import random 

word_list = ['Mango','Banana','Apple','Kiwi','Strawberry']

guess = input("Guess a Letter")

if guess.isalpha() & len(guess) == 1:
    word = random.choice(word_list)
    print(word)
else:
    print("Oops! That is not a valid input.")
    
In this milestone I firstly imported a package called random. This package randomly generates words from the given list. In this case the given list is word_list. I have assignmed 5 fruits to this list. In the next line i have asked for an input and assigned it to 'guess'. I have then created an if statment which will check 'guess' the input given is an alphabect and only one character. If this is true, it will display a randon fruit, if this is false, it will say "Oops! That is not a valid input.". 
