'''
Created on Oct 10, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n == 0:
        return False
    if n % 2 == 1:
        return True
    else:
        return False
    
'''
42 converted to base-2 is 101010
'''
   
'''
~If you are given an odd base-10 number, the least significant bit (or the rightmost bit) will be 1.
~If you are given an even base-10 number, the least significant bit (or the rightmost bit) will be 0.
'''
   
'''
If you eliminate the least significant bit in a base-2 number, convert it to a base-10 number(n) and then do int(n / 2). 
For an example:
~if you have 1110(14) and take away the 0, then you are left with 111(7) (14/2 = 7)
~if you have 1111(15) and take away the 1, then you are left with 111(7). (15/2 = 7.5 = 7 [because its an int]).
'''

'''
We can easily find the base-2 representation of N, if it is odd, by using the steps as followed above on the second bullet point.
We can easily find the base-2 representation of N, if it is even, by using the first bullet point above.
'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'

print(numToBinary(0))
print(numToBinary(1))
print(numToBinary(4))
print(numToBinary(10))
print(numToBinary(42))
print(numToBinary(100))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return binaryToNum(s[0:-1]) * 2 + int(s[-1])

print(binaryToNum("100"))
print(binaryToNum("1011"))
print(binaryToNum("00001011"))
print(binaryToNum(""))
print(binaryToNum("0"))
print(binaryToNum("1100100"))
print(binaryToNum("101010"))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '':
        return 0
    elif s == '11111111':
        return '00000000'
    else:
        v = binaryToNum(s[0:-1]) * 2 + int(s[-1])
        m = v + 1
        if isOdd(m):
            result =  numToBinary(m // 2) + '1'
        else:
            result =  numToBinary(m // 2) + '0'
    p = (len(s) - len(result)) * '0'
    return p + result

print(increment('00000000'))
print(increment('00000001'))
print(increment('00000111'))
print(increment('11111111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return 
    return count(increment(s), n - 1)

print(count("00000000", 4))
print(count("11111110", 5))

'''
The Ternary Representation of 59 is:
59 / 3 = 19 R2
19 / 3 = 6 R1      ==> work from the bottom up to get: 2012
6 / 3 = 2 R0
          2
'''

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n < 3:
        return str(n)
    return numToTernary(n // 3) + str(n % 3)
    

print(numToTernary(42))
print(numToTernary(4242))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])

print(ternaryToNum('1120'))
print(ternaryToNum('12211010'))