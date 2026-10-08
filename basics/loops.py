#loops


#for loop
#To print a series of numbers from 0-4 or 1-50, we use range as sequence as shown below 2 examples.

print("*************************")
for i in range(5):
    print(i)

print("*************************")
for i in range(1,51):
    print(i)

#To print a series of numbers in reverse order from 50-1, we have to give the step value as -1 as shown below example.

print("*************************")
for i in range(50,0,-1):
    print(i)

#To print a serious of values from the given list of array, below is the example

print("*************************")
list = [10,20,30,"JS","TS","python","Java"]

for element in list:
    print(element)




print("*************************")
#break

for i in range(5):
    if i==3:
        break
    print(i)


print("*************************")
#continue

for i in range(5):
    if i==3:
        continue
    print(i)


print("*************************")
#pass

for i in range(5):
    if i==1:
        pass #do nothing
    print(i)



#while loop
print("*************************Whileloop")

i=1

while i<6:
    print(i)
    i=i+1


# A program to attempt username multiple times and print the outcome using while loop.

print("*************************AttemptUsernamePassword")

attempt = 0

username ="Python"

while attempt <=3:
    if(attempt ==3):
        print("Your account has been locked")
        break;
    else:
        print("Please enter correct username or password")
    attempt = attempt+1



#Assignment:

print("*********************AssignmentIdenVowels")

str = '''This is a Python String
write a program to print only vowel part of the string
'''
vowels = "aeiouAeiou"
print(str)

print("*********************Output:")

for char in str:
    if char in vowels:
        print(char)
