'''
Created on Sep 5, 2018

@author: ameye
'''
from cs115 import map, reduce, range 

def add(x, y):
    '''returns x + y'''
    return x + y

def square(x):
    '''returns the square of x'''
    return x * x

def mult(x, y):
    '''returns x * y'''
    return x * y

def span(lst):
    '''Returns the difference between the maximum and the minimum numbers in a list.'''
    return reduce(max, lst)- reduce(min, lst)

def gauss(n):
    '''Takes as input a positive integer in and returns the sum: 1+2+3+...n'''
    return reduce(add, range(1, n + 1))

def sum_of_squares(n):
    '''Takes as input a positive integer in and returns the sum: 1^2 + 2^2 + 3^2... n^2'''
    return reduce(add, map(square, range(1, n + 1)))
                  
print(gauss(5))
print(span([1,2,3,4,5,6]))
print(sum_of_squares(5))
print(reduce(mult,[1,2,3,4,5]))

sentence = ['hello','fuck','you','Ishaan']
print(reduce(max,map(len,sentence)))