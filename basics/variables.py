# Is a single line comment

'''
Is a 
Multiline
comment
'''

"""
Also is a
Multiline
comment
"""

print("Welcome to AILLM")

#To Execute
# python basics/variables.py

var = 10 #Global scoped variable

def fun():
    var1 =70 # local scoped variable
    print (var)
    print (var1)

fun()

print(var)
#print (var1) #NameError: name 'var1' is not defined.
