'''
Created on Sep 5, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Andrea Meyer
username: ameyer
'''
from cs115 import map, reduce
import math

def sub(x, y):
    '''returns x-y'''
    return x - y

def inverse(n):
    '''Takes as input an integer, n, and returns the reciprocal'''
    return float(1/n)

def e(n):
    """Approximates the mathematical value e"""
    return sum(map(inverse, map(math.factorial, range(0, n+1))))

def error(n):
    '''returns the absolute value, of the difference between the actual value of e and e(n)'''
    return abs(sub(math.e, e(n)))

print(inverse(4))
print(e(10))
print(error(3))