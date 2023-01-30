# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

MILESTONE 1
In milestone 1 I have connected my github to the Aicore portal in order to create a repo with hangman folder. 

MILESTONE 2
import random 

word_list = ['Mango','Banana','Apple','Kiwi','Strawberry']

guess = input("Guess a Letter")

if guess.isalpha() & len(guess) == 1:
    word = random.choice(word_list)
    print(word)
else:
    print("Oops! That is not a valid input.")
    
Above is the code i have used for completing this milestone. 
    
In this milestone i first has to connect the github repo to my local machine so that i could create and edit files. Github is a way to use git in a distributed way, you can easily share code online as well as locally. To connect to github I had to use the Git Clone command. In order to use this command, i had to get the link from hitgub, which can be found under 'code'. I copied this link and run 'git clone LINK' in the terminal, this created a remote repositary. As this is the first time i ever used github with my local machine, i was asked the the github username and a password. I entered my email and password same as the login for github, but this did not work. I continued to do some research on this and learned that i need to create and enter and API key which can be created through the settings in github. I entered this API key into the password and this linked the github account to local machine, downloading the repo. Anything done in this repo, i can modify, stage and commit the changes and use the 'git push' command to update it on github. Portal will then have access to check the code. 

One of the first tasks was to create a list containing the name of 5 fruits. I assigned this list to 'word_list'. I then went ahead and printed it to check that it was working correctly, this output the fruits on the screen. In the next task i had to import a new module called random. This random module generates random word from the given list, which in this case is 'word_list'. This is perfect hangman because we will need this to generate a random word when someone is playing it. In the next next i had to create a random.choice and pass the word_list to it and assigned this to a variable called 'word'. This line of code allows anything in the list 'word_choice' to be generated at random. i then followed this with a print(word) to make sure this works correctly. I then run this code a few times and saw the output was a random word from the list, with no pattern to it, which is correct for hangman. 

The next task was to create and valildate the input. Firstly i got the input and assinged it to a varibale called 'guess'. Then i used a if statement to check the valiation of the input and only if the input is correct, then it will run the random module to generate a randon word from the list. I used build in methods from python to check the input is an alphabect and only 1 character long. If this is true, then it will generate and print a random word, or it will print "Oops! That is not a valid input.". 

MILESTONE 3

import random 

word_list = ['mango','banana','apple','kiwi','strawberry']
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

def ask_for_input():   
    while True:
        guess = input('Guess a Letter')
        if guess.isalpha()==True and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input() 

In this milestone, I made two functions from which one will ask for the input and validate it, and the other would take the input and check if its in the word and display a message accordingly. In the first function which is called Check_guess. I have passed the varibale guess to this functions so that this funciton will take the value of guess and use it in the function. Then it will take the guess, and convert it to lowercase, Then it will check if this letter is in the randomly generated word and if it is, it will say 'Good guess! {guess} is in the word', otherwise it will say Sorry, {guess} is not in the word. Try again. The second function will run while true, which means it will run continuously. Then it will check the letter given is an alphabect and the length is euqal to one. If those are true, at this stage, the loop will break and if its not, it will display 
'Invalid letter. Please, enter a single alphabetical character'. Functions do not run unless they are called, therefore i then called both of the functions. 


MILESTONE 4 

import random 
word_list = ['mango','banana','apple','kiwi','strawberry']

class Hangman:

    def __init__(self, word_list, num_lives = 5):
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
        
myInstance = Hangman(word_list)
print(myInstance.word)
print(len(myInstance.word_guessed))
print(myInstance.num_lives)
myInstance.ask_for_input()

The code for this milestone is above. In this milestone we implemented OOP. This means using classes for hangman. First I made an initalise class in which i have define all the attributes. 

Firstly i created a method whcih check check that the guess was in the word that was randomly chosen. In order to do this successfully, I firsty converted the letter entered to a lower case to make the running of the code smoother. Then i check if the letter guessed (guess) is in the self.word, which is the word that has been chosen. If the letter is in the code, then it will reduce the number of guesses left (default is 5) by one and display a message saying good guess. If the letter is not in the word, then it will again, reduce the guesses left and display that this letter is not in the word, and show a number of guesses left. Then finally for this method, the last line of code, which is outside the loop to make sure it applies to either of the outputs, adds the letter to the list which we have create in attributes above. 

Another method that i made was to get the input and validate it. If the input was not an alphabect && not equals to one character then it will display an error message saying "Invalid letter. Please, enter a single alphabetical character.". Then it will check if the guess is in the list of guesses that have already been made. This is to make sure that the player does not enter the same letter more than once. If it has been entered before, it will display a message saying you have already tried that letter. If the letter is an alphabect and one character, and it has not already been used before, then it will run the check guess method. 