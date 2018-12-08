'''
Created on Oct 29, 2018
I pledge my honor that I have abided by the Stevens Honor System.
@author: Andrea Meyer
@author: ameye
'''
def map_sqr(lst):
    '''Assume lst is a list, that returns map(sqr, lst)'''
    result = []
    for x in lst:
        result.append(x * x)
    return result

def map_lst_comprehenstion(lst):
    '''Assume lst is a list, that returns map(sqr, lst)'''
    return [x*x for x in lst]

def find_max(lst):
    '''Return the maximum element of the list'''
    if lst == []:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x 
    return max_val

def find_min(lst):
    '''Returns a touple of the min and max elements in the list'''
    if lst == []:
        return None
    min_val = max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x 
        elif x < min_val:
            min_val = x 
    return (min_val, max_val)
            

print(map_sqr([1, 2, 3]))
print(map_lst_comprehenstion([1, 2, 3]))
print(find_min([5, 6, 1, 3, 8, 4, 2]))

def shallow_copy(lst):
    result = []
    for x in lst:
        result.append(x)
    return result

def shallow_copy_comprehension(lst):
    return [x for x in lst]

def deep_copy(lst):
    new_lst = []
    for x in lst:
        if type(x) is lst:
            new_lst.append(deep_copy(x))
        else:
            new_lst.append(x)
    return new_lst

def sequential(key, lst):
    '''Returns the values of the key in lst, if found, and -1 otherwise'''
    for i in range(len(lst)):
        pass
    
def binary_search(lst ,key):
    low = 0
    high = len(lst)-1
    while high >= low:
        mid = low + (high - low) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1 
        else:
            return mid 
    return -low - 1

def swap(lst, a, b):
    '''swaps lst[a] with lst[b]'''
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    
    '''selection sort always makes (n(n-1))/2 comparisons; makes at most (n-1) swaps'''
    
def selection_sort(lst):
    '''sorts the list the 0(n^2) selection sort algorithm'''
    n = len(lst)
    for i in range(n-1):
        min_index = i 
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j 
            if min_index != i: 
                swap(lst, i, min_index)
    