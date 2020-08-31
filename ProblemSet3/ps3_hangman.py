# -*- coding: UTF-8 -*-
# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)  
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

#-------------------------------------------------

wordlist = loadWords()


#判断猜测的字母是否覆盖要猜测的单词,也就是是否猜测完毕

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    n = 0
    for i in secretWord:
        if i in lettersGuessed:
            n +=1
    if n == len(secretWord):
        return True
    else:
        return False

#secretWord = 'eikpr'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print isWordGuessed(secretWord, lettersGuessed)

# 获得单词中已经猜测到的单词，猜到的显示出来，没有猜到的用'_'代替

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guss = []
    for i in secretWord:
        if i in lettersGuessed:
            guss.append(i)
        else:
            guss.append('_ ')
    return ''.join(guss)

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getGuessedWord(secretWord, lettersGuessed)






# 返回可供选择的单词，如果一个单词已经猜过，就不会再出现

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    retlist = []
    import string
    abcList = string.ascii_lowercase

    for i in abcList:
        if i not in lettersGuessed:
            retlist.append(i)
    return ''.join(retlist)
# test code
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print getAvailableLetters(lettersGuessed)
    

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
    # FILL IN YOUR CODE HERE...

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord)) +' letters long.')
    print ('-------------')
    #准备工作完成
    #----------------------------------------------------------------------------------
    
    
    
    lettersGuessed = []
    i = 8 
    while i > 0:

        print('You have '+ str(i) + ' guesses left.')
        print 'Available Letters:', getAvailableLetters(lettersGuessed)
        
        #接受输入的的字符
        lettersInput = raw_input('Please guess a letter: ')
        
        guss = lettersInput.lower()   #将输入的字符小写化
        
        #首先检测是否输入过 如果输入过，提示，不加数，没有的话，
        if guss in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
            print ('-------------')
            continue
        else:
            lettersGuessed.append(guss)
        
        #没有输入这个字母
        
        if guss in secretWord:
                print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
                print ('-------------')
            
        else:
            i -=1
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
            print ('-------------')
        
        #判断是否达到边界
        # 如果完全猜出
        if  isWordGuessed(secretWord, lettersGuessed):          
            print ('Congratulations, you won!')
            break 
        if i == 0:
            print('Sorry, you ran out of guesses. The word was else. The word is :',secretWord)
            
    
          

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#从 worldlist 中随机选择一个小写 word

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
