#Set - {}


set1 = {1,2,3,4,"Java", "JS", "TS", 40,20,30,10}
print(set1)

#We can convert list to set - to tuple and vice versa

list = [1,2,3,4,"TS","JS",1,2,3,4,10,20,30]
print(list)

set2 = set(list)
print(set2)

#How to get elements from the set using looping concept

for value in set1:
    print(value)


#add the element in set by - add()

set3 = {"TS","JS",10,20,30}

set3.add(4)
print(set3)


#add the element in set by - update()

set3.update([7])
print(set3)


#Remove()

set3.remove(4)
print(set3)

#discard()

set3.discard(100)
print(set3)


#pop()

set3.pop()
print(set3)

#clear()

set3.clear()
print(set3)