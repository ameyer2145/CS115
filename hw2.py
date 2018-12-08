'''
Created on Sep 16, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
import sys
from cs115 import map, reduce, filter

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
#Helper Functions
def length_str(s):
    '''Returns the length of the list'''
    if s == []:
        return 0
    return 1 + length_str(s[1:])

def remove(e,L):
        '''Removes the first occurrence of search term in list'''
        if (L==[]):
            return []
        elif (L[0] != e):
            return [L[0]] + remove(e,L[1:])
        elif (L[0] == e):
            return L[1:]
        
def dictCheck(S):
        '''Checks if list member S is in the dictionary/returns point value.'''
        if (S==[]):
            return []
        elif (S[0] == ''):
            return []
        elif(S[0] in Dictionary):
            return [[S[0]] + [wordScore(S[0],scrabbleScores)]] + dictCheck(S[1:])
        else:
            return dictCheck(S[1:])
        
def rackCheck(Rack,S):
        '''Checks if string S can be made up from letters in list Rack'''
        if (S==''):
            return ''
        elif (S[0] in Rack):
            NewRack = remove(S[0],Rack)
            n = rackCheck(NewRack,S[1:])
            return (S[0] + n)
        else:
            return '0'
# Implement your functions here.
def letterScore(letter, scorelist):
    '''Returns a number that is associated with a letter'''
    result=filter((lambda x: x[0]==letter),scorelist)
    return result[0][1]
print(letterScore("c", scrabbleScores))
print(letterScore("a", scrabbleScores))

def wordScore(S, scorelist):
    '''Takes as input a string and a scorelist and returns the scrabble score of that string'''
    if (S==''):
        return 0
    elif ((letterScore(S[0],scorelist))):
        return (letterScore(S[0],scorelist)) + wordScore(S[1:],scorelist)
print(wordScore('spam', scrabbleScores))
print(wordScore("wow", [['o', 10], ['w', 42]]))

def scoreList(Rack): 
    '''Takes as input, rack, and returns a list of all the words in the global Dictionary'''
    def wordTest(Rack,L):
        '''Tries each word in dictionary against rack and sees if string is possible to create from rack'''
        if (L==[]):
            return L
        elif ('0' not in rackCheck(Rack,L[0])):
            return [L[0]] + wordTest(Rack,L[1:])
        else:
            return wordTest(Rack,L[1:])
    words = wordTest(Rack,Dictionary)
    return dictCheck(words)
print(scoreList(["a", "s", "m", "t", "p"]))
print(scoreList(["a", "s", "m", "o", "f", "o"]))

def bestWord(Rack):
    '''Takes as input, rack, and returns the highest scoring word and its score'''
    def maxScore(L):
        '''Returns the best word/word with highest point value given a list formatted like output from scoreList'''
        if L == [] or L == '':
            return 0
        elif (length_str(L)==1):
            return L[0]
        else:
            L[0] = L[1]
            return maxScore(L[1:]) 
    if maxScore(scoreList(Rack)) == 0:
        return ['', 0]  
    else:
        return maxScore(scoreList(Rack))
print(bestWord(["a", "s", "m", "t", "p"]))
print(bestWord(['g', 'y', 'e']))