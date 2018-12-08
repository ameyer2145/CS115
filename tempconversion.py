'''
Created on Aug 29, 2018

@author: ameye
'''


'''This function takes the fahrenheit value and converts it into Celcius'''
def celcius(temp):
    return 5/9(temp-32)

'''This function takes the Celcius value and converts it into Fahrenheit''' 
def fahrenheit(temp):
    return (9/5)*temp + 32

''' 
Call the functions below the function definitions
''' 
c = float(input("Enter degrees in Celcius: "))
f = fahrenheit(c)
#You can print multiple items in the statement. If you put a comma after each item, it prints a space 
#and then does on to print the next item.

print(c, 'C =', f, 'F')
#You can print this way too, but allowing exactly two decimal places
print('%.2f C = %.2f F' % (c, f))

f = float(input('Enter degrees in Fahrenheit: '))
c = celcius(f)
print(f, 'F =', c, 'C')
print('%.2f F = %.2f C' % (f, c))

'''
Try composition of fuctions.
Converting a Fahreheit temperature to Celcius and back to Fahrenheit should give you the original 
temperature
'''

print() #this prints a new line
f = float(input('Enter degrees in Fahrenheit: '))

#Use assert to check the returned value is equal to the expected value
assert fahrenheit(c(f)) == f
#No output should be produced, unless the assertion fails, which means you have an error
