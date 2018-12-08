'''
Created on Oct 25, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
def TcToNum(n):
    '''Takes as input a string of 8 bits representing an integer in two's-complement, and returns the corresponding integer'''
    def TcToNumHelper(n):
        if n == '':
            return 0
        return TcToNumHelper(n[:-1]) * 2 + int(n[-1])
    if n[0] == '0':
        return TcToNumHelper(n[1:])
    else:
        return TcToNumHelper(n[1:]) - 128
    
print(TcToNum("00000001"))
print(TcToNum("11111111"))
print(TcToNum("10000000"))
print(TcToNum("01000000"))

def NumToTc(n):
    '''takes as input an integer N, and returns a string representing the two's-complement representation of that integer'''    
    if n < -128 or n > 127:
        return "Error"
    if n < 0:
        n = -n
    bin1 = '{0:08b}'.format(n)
    return bin1
    
print(NumToTc(1))
print(NumToTc(-128))
print(NumToTc(200))