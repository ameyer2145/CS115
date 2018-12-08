'''
Created on Oct 17, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''

def numToBaseB(N,B):
    '''takes as input a non-negative integer N and a base B (2 and 10), and returns a string representing
    the number N in base B'''
    if N == 0: 
        return '0'
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))
    
print(numToBaseB(4, 2))
print(numToBaseB(4, 3))
print(numToBaseB(4, 4))
print(numToBaseB(0, 4))
print(numToBaseB(0, 2))

def baseBToNum(S,B):
    '''takes as input a string S and a base B, and returns an integer in base 10 representing S'''
    if S == '':
        return 0
    return baseBToNum(S[0:-1], B) *B + int(S[-1])

print(baseBToNum("11", 2))
print(baseBToNum("11", 3))
print(baseBToNum("11", 10)) 
print(baseBToNum("", 10))

def baseToBase(B1,B2,SinB1):
    '''converts SinB1 from base B1 to base B2'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

print(baseToBase(2, 10, "11"))
print(baseToBase(10, 2, "3"))
print(baseToBase(3, 5, "11"))

def add(S,T):
    '''takes as input two binary strings and returns in their sum in binary'''
    return numToBaseB(int(baseBToNum(S, 2) + baseBToNum(T, 2)), 2) 

print(add("11", "01"))
print(add("011", "100"))
print(add("110", "011"))

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addB(S, T):
    '''Returns the addition of two binary strings in binary'''
    def addB_helper(s, t):
        '''Returns the carry of the addition of s and t in binary'''
        if s =='' or t == '':
            return '0'
        elif s == '0' or t == '0':
            return '0'
        else: 
            return '1'
    if S == '':
        return T
    if T == '':
        return S
    else:
        return addB(S[:-1], T[:-1]) + FullAdder[S[-1], T[-1], addB_helper(S[-1], T[-1])][0]
    
print(addB("11", "1"))
print(addB("011", "100"))