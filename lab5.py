'''
Created on Oct 3, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
import time
from cs115 import map

words = []
HITS = 10

def ED(first, second):
    ''' Returns the edit distance between the strings first and second.'''
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]:
        return ED(first[1:], second[1:])
    else:
        substitution = ED(first[1:], second[1:])
        deletion = ED(first[1:], second)
        insertion = ED(first, second[1:])
        return 1 + min(substitution, deletion, insertion)
    
print(ED("spam", "xsam"))
print(ED("foo", ""))
print(ED("foo", "bar"))
print(ED("hello", "below"))
print(ED("yes", "yelp"))

def fastED(s1, s2):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastED_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if s1 == '':
            return len(s2)
        if s2 == '':
            return len(s1)
        elif s1[0] == s2[0]:
            result = fastED_helper(s1[1:], s2[1:], memo)
        else:
            substitution = fastED_helper(s1[1:], s2[1:], memo)
            deletion = fastED_helper(s1[1:], s2, memo)
            insertion = fastED_helper(s1, s2[1:], memo)
            result = 1 + min(substitution, deletion, insertion)
        memo[(s1, s2)] = result
        return result
    return fastED_helper(s1, s2, {})
print(fastED("antidisestablishment", "antiquities"))
print(fastED("xylophone", "yellow"))
print(fastED("follow", "yellow"))
print(fastED("lower", "hover"))


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda word: (fastED(user_input, word), word), words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()