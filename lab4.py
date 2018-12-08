'''
Created on Sep 26, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
def knapsack(capacity, itemList):
    '''Takes in a list of pairs (first number represents the weight, and the second number represents
    the value of each item) and returns both the maximum value and the list of items that make this value'''
    if itemList == [] or capacity == 0:
        return [0,[]]
    if capacity - itemList[0][0] < 0:
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity - itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    if itemList[0][1] + use_it[0] >= lose_it[0]:
        return [itemList[0][1] + use_it[0]] + [[itemList[0]] + use_it[1]]
    else:
        return [lose_it[0]] + [lose_it[1]]
    
print(knapsack(6, [[1, 4], [5, 150], [4, 180]]))
print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(25, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]))
print(knapsack(20, []))
print(knapsack(0, [[1, 1000], [2, 3000], [4, 55000]]))