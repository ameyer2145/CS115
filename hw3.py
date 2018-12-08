'''
Created on Sep 20, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import map
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''HW2 Functions'''
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
        
def letterScore(letter, scorelist):
    '''Returns a number that is associated with a letter'''
    result=filter((lambda x: x[0]==letter),scorelist)
    return result[0][1]

def wordScore(S, scorelist):
    '''Takes as input a string and a scorelist and returns the scrabble score of that string'''
    if (S==''):
        return 0
    elif ((letterScore(S[0],scorelist))):
        return (letterScore(S[0],scorelist)) + wordScore(S[1:],scorelist)

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


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return map(lambda S: [S, wordScore(S, scores)], dct)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if L[0] == n:
        return []
    return list(range(L[0], n))
print(take(3, [0, 1, 2, 3, 4, 5, 6]))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if L[0] == n:
        return [L[0]] + L[1:]
    return list(range(n, len(L)))
print(drop(3, [0, 1, 2, 3, 4, 5, 6]))
'''PDF'''
def giveChange(numberofCoins, listofCoins):
    '''Takes the same input as change(), but returns a list whose first item is the minimum number of coins,
    and the second item is a list of coins in that optimal solution'''
    if numberofCoins == 0:
        return [0, []]
    if listofCoins == []:
        return [float("inf"), []]
    if listofCoins[0] > numberofCoins:
        return giveChange(numberofCoins, listofCoins[1:])
    [use_it_amt, use_it_list] = giveChange(numberofCoins - listofCoins[0], listofCoins)
    [lose_it_amt, lose_it_list] = giveChange(numberofCoins, listofCoins[1:])
    if use_it_amt+1 < lose_it_amt:
        use_it_list.append(listofCoins[0])
        return [use_it_amt+1, use_it_list]
    else:
        return [lose_it_amt, lose_it_list]

print(giveChange(48, [1, 5, 10, 25, 50]))
print(giveChange(48, [1, 7, 24, 42]))
print(giveChange(35, [1, 3, 16, 30, 50]))