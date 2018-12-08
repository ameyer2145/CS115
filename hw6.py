'''
Created on Oct 10, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
from cs115 import map, reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

#Helper Functions
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n == 0:
        return False
    if n % 2 == 1:
        return True
    else:
        return False

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return binaryToNum(s[0:-1]) * 2 + int(s[-1])

def add(x, y):
    """Returns x + y"""
    return x + y

def binaryLength(s):
    """returns a binary number that is the correct bit-length"""
    if len(s) >= COMPRESSED_BLOCK_SIZE:
        return s
    else:
        return binaryLength('0'+s)
    
def compressCount(S):
    """Returns the count of how many times the first integer is consecutive"""
    if S == '':
        return 0
    elif len(S) == 1:
        return 1
    elif S[0] == S[1]:
        return 1 + compressCount(S[1:])
    else:
        return 1
    
def compressList(S):
    """Returns a list of the values of the consecutive integers in succession"""
    if S == '':
        return []
    return [compressCount(S)] + compressList(S[compressCount(S):])

def compressBreak(L):
    """Breaks the numbers up so they are not larger than the maximum run length"""
    if L == []:
        return []
    if L[0] > MAX_RUN_LENGTH:
        L[0] = L[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + compressBreak(L)
    return [L[0]] + compressBreak(L[1:]) 

# Write your functions here. You may use those variables in your code.
def compress(S):
    '''Takes as input a binary string, s, of length 64 and returns another binary string output. The output 
    string should be a run-length encoding of the input string'''
    if S == '':
        return ''
    elif S[0] == '1':
        return '0' * COMPRESSED_BLOCK_SIZE + reduce(add, map(binaryLength, map(numToBinary, compressBreak(compressList(S)))))
    else:
        return reduce(add, map(binaryLength, map(numToBinary, compressBreak(compressList(S)))))
    
sequence = '1' * 64
print(compress(sequence))

def uncompress(C):
    '''Inverts/Undoes the compressing in compress(S)'''
    def uncompressHelp(n, s):
        if s == '':
            return ''
        elif n == 1:
            return binaryToNum(s[:5]) * '1' + uncompressHelp(0, s[5:])
        elif n == 0:
            return binaryToNum(s[:5]) * '0' + uncompressHelp(1, s[5:])
    if C == '':
        return 0
    return uncompressHelp(0, C)

'''
The is the largest number of bits that the compress algorithm could possibly use to encode a 64-bit string/image, would
be 384. Since there is a max string limit of 64, we would just have to convert 64 to 1000000, which is 2^6. 6 multiplied
by 64 is 384.
'''
    
def compression(S):
    '''returns the ratio of the compressed size to the original size for image S'''
    return len(compress(S))/len(S)

'''
The compression tests with the images of Penguin, Smile and Five have shown that the compression algorithm
will make compressed strings that are longer than the input string length, which results the ratio between
them to be greater than one.
'''

'''
Professor Lai is lai-ing (the algorithm cannot exist). There are some instances where the ratio between the compressed string and
the initial string is less than 1. But, in situation where the combination between strings are greater than 64-bits, then the ratio
is larger and therefore the algorithm cannot exist.
'''

#Penguin
print(compression("00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"))

#Smile
print(compression("0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8))

#Five
print(compression("1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"))

print(compression("1" * 64))