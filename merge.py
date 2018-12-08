'''
Created on Nov 9, 2018
I pledge my honor that I have abided by the Stevens Honor System
@author: Andrea Meyer
username: ameyer
'''
def num_matches(list, list2):
    '''Returns the number of elements that the two lists have in common'''
    list.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list) and j < len(list2):
        if list[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches
    
def keep_matches(list, list2):
    '''Returns a list of the elements that the two lists have in common'''
    list.sort()
    list2.sort()
    result = []
    i = j = 0
    while i < len(list) and j < len(list2):
        if list[i] == list2[j]:
            result.append(list[i])
            i += 1
            j += 1
        elif list[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

def drop_matches(list, list2):
    '''Returns a new list that contains only the elements in list2 that are NOT in list'''
    list.sort()
    list2.sort()
    result = []
    i = j = 0
    while i < len(list) and j < len(list2):
        if list[i] == list2[j]:
            i += 1
            j += 1
        elif list[i] < list2[j]:
            i += 1
        else:
            result.append(list[j])
            j += 1
    while j < len(list2):
        result.append(list[i])
        j += 1
    return result

A = [2, 3, 5, 7, 9, 11, 13, 17, 23]
B = [11, 13, 15, 17, 19, 21, 23, 25, 27]  
print(num_matches(A, B))
print(keep_matches(A, B))
            