'''
Created on Sep 10, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Andrea Meyer
username: ameyer
'''
from cs115 import map, range, reduce, filter
import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n -1)

def tower(n):
    '''Computes 2^(2^(2...))) n times'''
    if n == 0:
        return 1
    return 2 ** tower(n - 1)
print(map(tower, range(6)))

def tower_reduce(n):
    '''Computes 2^(2^(2...))) n times using reduce'''
    def power(x, y):
        return y ** x
    return reduce(power, [2] * n)
print(map(tower_reduce, range(1, 5)))

def length(lst):
    '''Returns the length of the list'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])
print(length([1, 2, 5, 6, 7]))

def length_str(s):
    '''Returns the length of the list'''
    if s == '':
        return 0
    return 1 +length_str(s[1:])
print(length_str('moviepass'))

def reverse(lst):
    '''Takes as input a list of elements and returns the list in reverse'''
    if lst == []:
        return []
    #return reverse(lst[1:]) + [lst[0]]
    return [lst[-1]] + reverse(lst[:-1])
print(reverse([1, 4, 9]))

def member(x, lst):
    '''Returns true if x is contained in the list and False otherwise'''
    '''Tail Recursive Function'''
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])
print(member(5, [1, 2, 3]))

def collapse(lst):
    '''Collapses a lists of possibly nested lists into a single list of values'''
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])
print(collapse([1, [2, 3], [5], 4]))

def myMap(f, lst):
    '''Returns a new list where the function, f, has been applied to every element in the original list'''
    if lst == []:
        return []
    return [f(lst[0])] + myMap(f, lst[1:])
def sqr(x):
    return x * x
print(myMap(sqr, [1, 2, 3]))

def power(x, y):
    '''Returns x^y'''
    if y == 0:
        return 1
    return x * power(x,y - 1) #Linear Recursion because we have a pending operation

def power_tail(x, y):
    '''Computes x^y with tail recursion'''
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x) 
    return power_tail_helper(x, y, 1)

def myReduce(f, lst):
    '''Reduces a new list where it has been reduced to a single value as dictated by the predicate f'''
    def myReduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return myReduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst == []:
        return TypeError('myReduce() or empty sequence with no initial value')
    return myReduce_helper(f, lst[1:], lst[0])
def add(x, y):
    return x + y
print(myReduce(add, [1, 2, 3]))

def prime(n):
    '''Returns whether or not an integer is prime'''
    possibleDivisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda X: n % X == 0, possibleDivisors)
    return len(divisors) == 0

def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x:x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n))
print(primes(100))

def fib(n):
   #Tree Recursion
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n-2)

def subset(target, lst):
    '''Determines whether or not it is possible to create target sum using the values in the list. Values
    in the list can be positive, negative or zero'''
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target,lst[1:])
    #dont use variables

def powerset(lst):
    '''Returns power set of the list that is, the ste of all subsets of the list'''
    if list == []:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

def subset_with_values(target, lst):
    '''Determines whether or not it is possible to create the target sum using values in the list. Values
    in the list can be positive, negative or zero. The function returns a tuple of exactly two items. The
    first is a boolean, that indicates True if the sum is possible and False if not. The second element
    in the tuple is a list of all the values that add up to make the target sum.'''
    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])
print(subset_with_values(5, [3, 1, 2]))

def LCS(s1, s2):
    '''Returns the length of the longest common subsequence in strings, s1 and s2.'''
    if s1 == '' or s2 == '':
        return 0
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
print(LCS('stocks', 'rocks'))
print(LCS('stop', 'losses'))

def LCS_with_values(s1, s2):
    if s1 == '' or s2 == '':
        return [0, '']
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return [1 + result[0], s1[0] + result[1]]
    uses1 = LCS_with_values(s1, s2[1:])
    uses2 = LCS_with_values(s1[1:], s2)
    if uses1[0] > uses2[0]:
        return uses1
    return uses2
print(LCS_with_values('pole', 'poke'))

def coin_row(lst):
    '''Takes in a list and returns how much money can be picked up'''
    if lst == []:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))
print(coin_row([]))
print(coin_row([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def coin_row_with_values(lst):
    '''Takes in a list and returns how much money can be picked up, and what coins are selected'''
    if lst == []:
        return [0,[]]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it
print(coin_row_with_values([]))
print(coin_row_with_values([5, 1, 2, 10, 6, 2]))
print(coin_row_with_values([10, 5, 5, 5, 10, 50, 1, 10, 1, 1, 25]))

def distance(first, second):
    '''Insert DocString'''
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])
    deletion = distance(first, second[1:])
    insertion = distance(first[1:], second)
    return 1 + min(substitution, deletion, insertion)

    