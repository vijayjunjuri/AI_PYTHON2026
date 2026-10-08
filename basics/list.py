#list

list =[1,2,3,4,"Python","JS", True, 4.5,3,2,1]
print(list[3])

print(list[3:9])

print(list)

#for loop using list

print("***********************")

for ele in list:
    print(ele)


#update

list[6] = "TS"
print(list[6])
print(list)

#Delete the element from the list by using Index

#del list[3]
#print(list)

#Delete the element from the list by using direct element - remove keyword

#list.remove(4.5)
#print(list)

#list.remove("TS")
#print(list)

#pop() - which deletes the last element form the list

#list.pop()
#print(list)

#To add the element in the list

#append()

list.append(12)
print(list)

#Insert()

list.insert(3,"Java")
print(list)

#clear()

list.clear()
print(list)