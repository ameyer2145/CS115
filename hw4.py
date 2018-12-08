'''
Created on Sep 26, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
#HelperFunction
def pascal_add(lst):
    '''Creates a new list with the sum of the adjacent terms in the original list'''
    if lst==[]:
        return []
    if len(lst)==1:
        return [1]
    return [lst[0] + lst[1]] + pascal_add(lst[1:])

def pascal_row(num):
    '''As input a single integer, which represents a row number, and outputs a list of elements 
    found in a certain row in Pascal's Triangle'''
    if num == 0:
        return [1]
    if num == 1:
        return [1,1]
    return [1] + pascal_add(pascal_row(num - 1))
    
def pascal_triangle(num):
    '''Takes as input a single integer, n, and returns a list of lists containing all rows up to
     (and including) n'''
    if num == 0:
        return [[1]]
    if num == 1:
        return [[1], [1, 1]]
    return pascal_triangle(num - 1) + [pascal_row(num)]
print(pascal_row(6))