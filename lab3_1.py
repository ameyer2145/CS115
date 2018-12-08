'''
Created on Sep 19, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
  
def change(amount, coins):
    '''Takes as input an amount, that is a non-negative, and returns a non-negative number of minimum used 
    coins to make up the given amount'''
    if amount==0:
        return 0
    if coins== [] or amount < 0:
        return float('inf')
    else:
        useIt= change(amount - coins[0], coins)
        loseIt= change(amount,coins[1:]) + 1
    useIt.append(coins[0])
    return min(loseIt,useIt)

print(change(48, [1, 5, 10, 25, 50]))
print(change(48, [1, 7, 24, 42]))
print(float("inf") > 42)
print(42 + float("inf"))
print(min(42, float("inf")))