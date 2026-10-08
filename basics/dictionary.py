#Dictionary

dict1 = {"Name" : "Vijay", "Age" : 41, "Salary" : 1000000, "Gender" : "Male"}
dict2 = {1 : "One", 2 : "Two", 3 : "Three"}

print(dict1)
print(dict2)

#To fetch the value from the dictionary

#Way-1

print("*****************way-1")

print(dict1["Name"])
print(dict1["Salary"])
print(dict2[2])

#way-2

print("*****************way-2")

print(dict1.get("Name"))
print(dict2.get(3))

print("*****************Keys()")

print(dict1.keys())

print("*****************values()")

print(dict1.values())

print("*****************items()")

print(dict1.items())

print("*****************Using for loop")

for key in dict1:
    print(key)
    print(key, dict1[key])


print("*****************for - values")

for value in dict1.values():
    print(value)

print("*****************for - items,way-1")

for value in dict1.items():
    print(value)

print("*****************for - items-way-2")

for key,value in dict1.items():
    print(key,value)


# Add element inside the dictionary

print("*****************Add element")

dict1["Address"] = "Vijayawada"
print(dict1)

# Update the element inside the dictionary

print("*****************Update element")

dict1["Address"] = "NY"
print(dict1)

# Delete the element from the dictionary

print("*****************del dict[key]")

del dict1["Address"]
print(dict1)

print("*****************dict.pop(key)")

dict1.pop("Age")
print(dict1)

print("*****************dict.popitem()")

dict1.popitem()
print(dict1)

print("*****************dict.clear()")

dict1.clear()
print(dict1)



#Assignment
print("*****************Assignment")

'''
Input - abcdabcdabcd
write a program to print the reust as below
output - a3b3c3d3

'''

print("*****************Method1")

count=0
value ="abcdabcdabcd"
char_count = {}

for char in value:
    char_count[char] = char_count.get(char,0) + 1

print(char_count)
char_count = char_count.replace(":","")
print(char_count)


