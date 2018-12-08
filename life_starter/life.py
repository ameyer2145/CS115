#
# life.py - Game of Life lab
#
# Name: Andrea Meyer
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random, sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

#print(createBoard(5, 3))

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
#A = createBoard(5,3)
#printBoard(A)

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

#A = diagonalize(7,6)
#printBoard(A)

def innerCells(w,h):
    '''returns a 2d array of all live cells - with the value of 1 - except
    for a one-cell-wide border of empty cells (with the value of 0) around
    the edge of the 2d array.'''
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if (row != 0 and row != h-1) and (col != 0 and col != w-1):
                A[row][col] = 1
    return A

#A = innerCells(5,5)
#printBoard(A)

def randomCells(w,h):
    '''returns an array of randoly-assigned 1's and 0's except that
    the outer edge of the array is still completely emply'''
    A = innerCells(w, h)
    for row in range(h):
        for col in range(w):
            if A[row][col] == 1:
                A[row][col] = random.choice([0,1])
    return A

#A = randomCells(10,10)
#printBoard(A)

def copy(A):
    '''creates a deep copy'''
    copy = []
    for x in A:
        row = []
        for y in x:
            row.append(y)
        copy.append(row)
    return copy

#oldA = createBoard(2,2)
#printBoard(oldA)
#newA = copy( oldA )
#printBoard(newA)
#oldA[0][0] = 1
#printBoard(oldA)
#printBoard(newA)

def innerReverse(A):
    '''takes an old 2d array and then
    creates a new generation of the same shape and size'''
    result = copy(A)
    h = len(result)
    w = len(result[0])
    for row in range(h):
        for col in range(w):
            if  (row == 0 or row == h-1) or (col == 0 or col == w-1):
                result[row][col] = 0
            elif result[row][col] == 1:
                result[row][col] = 0
            else:
                result[row][col] = 1
    return result

#A = randomCells(8,8)
#printBoard(A)
#print()
#A2 = innerReverse(A)
#printBoard(A2)

def next_life_generation( A ):
    '''makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    '''
    result = []
    i = j = 0
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            sum = 0
            if i == 0 or i == len(A) - 1 or j == 0 or j == len(A[i]) - 1:
                row.append(0 * j)
                continue
            for neighbor_i in range(i - 1, i + 2):
                for  neighbor_j in range(j - 1, j + 2):
                    sum += A[neighbor_i][neighbor_j]
            if A[i][j] == 1:
                row.append(1 if sum - A[i][j] == 3 or sum - A[i][j] == 2 else 0)
            else:
                row.append(1 if sum - A[i][j] == 3 else 0)
        result.append(row)
    return result

#A = [ [0,0,0,0,0],
#[0,0,1,0,0],
#[0,0,1,0,0],
#[0,0,1,0,0],
#[0,0,0,0,0]]
#printBoard(A)
#print()
#A2 = next_life_generation( A )
#printBoard(A2)
#print()
#A3 = next_life_generation( A2 )
#printBoard(A3)