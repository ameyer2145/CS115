'''
Created on Sep 12, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Andrea Meyer
username: ameyer
'''
def length(lst):
    '''Returns the length of the list'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def length_str(s):
    '''Returns the length of the list'''
    if s == []:
        return []
    return 1 + length_str(s[1:])

def dot(L, K):
    '''Takes as input, L and K, and returns the product of the lists'''
    '''If there is an invalid dot operation, an error occurs. EX: print(dot([5,3], [6]), 30)
    returns 0.0 30'''
    if length(L) != length(K) or length(L) == 0:
        return 0.0
    return L[0]*K[0] + dot(L[1:], K[1:])

def explode(s):
    '''Takes a string as input and return a list of characters in that string'''
    if s == "":
        return []
    if isinstance(s[0], list):
        return explode(s[0]) + explode(s[1:])
    return [s[0]] + explode(s[1:])

def ind(e, L):
    '''Takes an element and a sequence, and returns which index where e first appears in the sequence'''
    if (L == [] or L == ''):
        return 0
    if e == L[0]:
        return 0
    return 1 + ind(e, L[1:])
    
def removeAll(e, L):
    '''Takes an element and a list, and returns the list without the elements present'''
    if e in L:
        if e == L[0]:
            M = [L[1]] + removeAll(e, L[2:])
        else:
            M = [L[0]] + removeAll(e, L[1:])
        return M
    return L

def myFilter(e, L):
    '''Takes the first input and decides whether its T/F, and takes the second input as a list, and 
    returns a new list'''
    if L == []:
        return []
    if e(L[0]) == True:
        return [L[0]] + myFilter(e, L[1:])
    return myFilter(e, L[1:])

def deepReverse(L):
    '''Takes as input a list o0f elements, and outputs the reversal'''
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])