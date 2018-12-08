'''
Created on Oct 3, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
import turtle

def square_spiral(walls):
    def square_spiral_helper(walls, distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    square_spiral_helper(walls, 20, 20, 0)

#square_spiral(30)

def oct_spiral(walls):
    def oct_spiral_helper(walls, distance, initial, count):
        if count == walls:
            turtle.done()
        else:
            turtle.left(45)
            turtle.forward(distance)
            oct_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    oct_spiral_helper(walls, 20, 5, 0)

oct_spiral(30)