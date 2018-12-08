'''
Created on Sep 12, 2018
I pledge my honor that I have abided by the Stevens Honor System.
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

# Implement your functions here.
       
def letterScore(letter, scorelist):
    '''Returns a number that is associated with a letter'''
    result=filter((lambda x: x[0]==letter),scorelist)
    return result[0][1]
print(letterScore('c', scrabbleScores))
print(letterScore('a', scrabbleScores))

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
    filtered_list = filter((lambda S: wordScore(S, scoreList(Rack))), Dictionary)
    mapped_list = map((lambda letter: [letter, letterScore(letter)]), filtered_list)
    return mapped_list
print(scoreList(["a", "s", "m", "t", "p"]))
print(scoreList(["a", "s", "m", "o", "f", "o"]))

def bestWord(Rack):
    '''Takes as input, rack, and returns the highest scoring word and its score'''
    def maxPts(x):
        if (len(x)==1):
            return x[0]
        elif (len(x[0][1] > x[1][1])):
            x[1] = x[0]
            return maxPts(x[1:])
        else:
            x[0] = x[1]
            return maxPts(x[1:])
    return maxPts(scoreList(len(Rack)))
print(bestWord(["a", "s", "m", "t", "p"]))