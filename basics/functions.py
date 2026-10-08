#Functions

#1. Non-parameterised and non-returning function

def welcome():
    print("Welcome to AI LLM Testing")
welcome()

#2. Non-parameterised and returning function

def message():
    a=10
    b=60
    c=a+b
    return c

result = message()
print(result)


#3. parameterised and non-returning function

def login(username, password):
    print("Enter the UserName: ", username)
    print("Enter the Password: ", password)

login("test","Password")


#4. parameterised and returning function

def check_status(expected, actual):
    return expected == actual

status_result = check_status(200,200)
print(status_result)

status_result1 = check_status(200,400)
print(status_result1)



# * - wild card symbol

def display(*a):
    print(a)

display(1,2,3,4,5,6,"Python")