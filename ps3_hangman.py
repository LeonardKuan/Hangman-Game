# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for k in range(0, len(secretWord)):
        if secretWord[k] in lettersGuessed and k+1 == len(secretWord):
            return True
            break
        elif secretWord[k] in lettersGuessed:
            continue
        else:
            return False
            break

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Word = ''
    for k in range(0, len(secretWord)):
        if secretWord[k] in lettersGuessed and k+1 == len(secretWord):
            Word = Word[:k] + secretWord[k]
            return Word
            break
        elif secretWord[k] in lettersGuessed:
            Word = Word[:k] + secretWord[k]
        elif secretWord [k] not in lettersGuessed and k+1 == len(secretWord):
            Word = Word[:k] + "_ "
            return Word
        else:
            Word = Word[:k] + "_ "

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    Unguess = ''
    for k in range(0, len(string.ascii_lowercase)):
        if string.ascii_lowercase[k] in lettersGuessed and k+1 == len(string.ascii_lowercase):
            return Unguess
        elif string.ascii_lowercase[k] not in lettersGuessed and k+1 == len(string.ascii_lowercase):
            Unguess = Unguess[:k] + string.ascii_lowercase[k]
            return Unguess
        elif string.ascii_lowercase[k] in lettersGuessed:
            continue
        else: 
            Unguess = Unguess[:k] + string.ascii_lowercase[k]


def hangman(secretWord):
        '''
        secretWord: string, the secret word to guess.
    
        Starts up an interactive game of Hangman.
    
        * At the start of the game, let the user know how many 
          letters the secretWord contains.
    
        * Ask the user to supply one guess (i.e. letter) per round.
    
        * The user should receive feedback immediately after each guess 
          about whether their guess appears in the computers word.
    
        * After each round, you should also display to the user the 
          partially guessed word so far, as well as letters that the 
          user has not yet guessed.
    
        Follows the other limitations detailed in the problem write-up.
        '''
        lettersGuessed = []
        guessNo = 8
        
        def Recurs(guessNo, lettersGuessed):
            print("------------")
            print("You have " + str(guessNo) + " guesses left.")
            print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
            
        def Check(guessNo):
            for k in range(0, len(secretWord)):
                if guess == secretWord[k]:
                    print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
                    Recurs(guessNo, lettersGuessed)
                    return guessNo
                elif guessNo == 1 and guess != secretWord[k] and k+1 == len(secretWord):
                    print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                    print("------------")
                    print("Sorry, you ran out of guesses. The word was " + secretWord)
                    return guessNo
                elif guess != secretWord[k] and k+1 == len(secretWord):
                    guessNo -= 1
                    print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                    Recurs(guessNo, lettersGuessed)
                    return guessNo
                else:
                    continue
            
        print("Welcome to the game, Hangman!")
        print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
        Recurs(guessNo, lettersGuessed)
        guess = input("Please guess a letter: ")
        
        lettersGuessed.append(guess)
        
        while isWordGuessed(secretWord, lettersGuessed) == False:
            guessNo = Check(guessNo)
            guess = input("Please guess a letter: ")
            while guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
                Recurs(guessNo, lettersGuessed)
                guess = input("Please guess a letter: ")
            lettersGuessed.append(guess)
                
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
            print("Congratulations, you won!")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)