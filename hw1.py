'''
Created on Sep 5, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Andrea Meyer
username: ameyer
'''
from cs115 import reduce
import math

def mult(x, y):
    '''returns the product of x and y'''
    return x * y

def add(x, y):
    '''returns the sum of x and y'''
    return x + y

def factorial(n):
    '''takes a positive integer as input n, and returns n!'''
    return math.factorial(n)

def mean(L):
    '''takes a list and returns the average'''
    return float((reduce(add, L))/len(L))

def divide(n):
    '''defines div inside the function and returns div'''
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''takes a positive integer, and returns T/F depending on its prime composition'''
    return sum(map(divide(n), range(2, n))) == 0

print(reduce(mult, [2, 3]))
print(reduce(mult, [2, 3, 4]))
print(reduce(mult, [1, 2, 3, 4]))
print(factorial(2))
print(mean([1, 2, 3]))
print(mean([1, 1, 1]))
print(mean([1, 2, 3, 4]))
print(divide(5)(2.5))
print(prime(1))