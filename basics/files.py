#Files

print("********************r-it reads the file")

file = open("prompt.txt", "r")
data = file.read()
print(data)

print("********************r+-it reads the file and has write permission")

file = open("prompt.txt", "r+")
data = file.read()
print(data)

print("********************W+-it can create new file if the file doestn't exist")

file = open("prompt1.txt", "w+")
data = file.read()
print(data)

print("******************** r,readline()")

file = open("prompt.txt", "r")
data = file.readline()
print(data)

print("******************** r,readlines()")

#seek(0) is to move the cursor to starting of the file.

file.seek(0)
data = file.readlines()
print(data)
file.close()

print("******************** a - append text in the files.")

file = open("prompt.txt", "a")
file.write("\nAppending new line to the file")
file.close()


print("******************** w - create new pdf file and write data in it")

file1 = open("prompt2.pdf", "a")
file1.write("\nThis is an AI LLM course")
print(file1)
file.close()

print("******************** with keyword - is another method to declare and open the file. it automatically closes the file")

with open("prompt2.pdf", "r") as fileData:
    data1 = fileData.read()
    print(data1)