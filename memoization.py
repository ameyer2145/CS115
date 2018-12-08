'''
Created on Oct 1, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
import time

'''Memoization:
1) If key is inside the dictionary, return the value associated with the key
2)Do Work! Recursively compute the answer and store the result in a local variable
3) store the result in the dictionary and return the result'''

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n-2)

start_time = time.time()
#print(fib(40))
print('fib computation time without memoization: %.2f s' % (time.time() - start_time))

def fib_memo(n):
    def fib_helper(n, memo):
        '''if n is in memo, return memo[n]'''
        if n in memo:
            return memo[n]
        '''Do work!'''
        '''Recursively compute the result and save in local variable'''
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 2, memo) + fib_helper(n - 1, memo)
        '''Store the result in memo and return the result'''
        memo[n] = result 
        return result
    return fib_helper(n,{})
start_time = time.time()
print(fib(40))
print('fib computation time without memoization: %.2f s' % (time.time() - start_time))

def LCS(s1, s2):
    '''Returns the length of the longest common subsequence in strings, s1 and s2.'''
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
print(LCS('stocks', 'rocks'))
print(LCS('stop', 'losses'))

def fast_LCS(s1,s2):
    def fast_LCS_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo(s1, s2)
        if s1 == '' or s2 == '':
            return 0
        elif s1[0] == s2[0]:
            result = 1 + LCS(s1[1:], s2[1:])
        else:
            result = max(LCS(s1, s2[1:]), LCS(s1[1:], memo),
                                fast_LCS_helper(s1[1:], s2, memo))
        memo[(s1, s2)] = result
        return result                        
        return fast_LCS_helper(s1, s2, {})
    
