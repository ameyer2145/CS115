'''
Created on Sep 19, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
  
def change(amount, coins):
    '''Takes as input an amount, that is a non-negative, and returns a non-negative number of minimum used 
    coins to make up the given amount'''
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    if coins[0] > amount:
        return change(amount, coins[1:])
    [use_it_amt, use_it_list] = change(amount-coins[0], coins)
    [lose_it_amt, lose_it_list] = change(amount, coins[1:])
    if use_it_amt+1 < lose_it_amt:
        use_it_list.append(coins[0])
        return [use_it_amt+1, use_it_list]
    else:
        return [lose_it_amt, lose_it_list]

print(change(48, [1, 5, 10, 25, 50]))
print(change(48, [1, 7, 24, 42]))
print(float("inf") > 42)
print(42 + float("inf"))
print(min(42, float("inf")))