#Class, Object, object constructor

class Employee:

    name: str
    age: int
    gender: str
    salary: float
    skills: list

    def __init__(self,name,age,gender,salary,skills):

        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.skills = skills

    def display_employee(self):

        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee Gender: ", self.gender)
        print("Employee Salary: ", self.salary)
        print("Employee Skills: ", self.skills)


obj = Employee("Vijay", 41, "Male", 1000000, ["Functional-NonFunctional-Security Automation", "Python", "JS", "TS", "AI LLM"])
obj.display_employee()
print("")
obj1 = Employee("Deepthi", 40, "Female",800000, ["BDS", "MDS"])
obj1.display_employee()


# Inheritance
#creating a child class to inherit properties & methods from Employee(parent) class

class Department(Employee):

    department : str

    def __init__(self,name,age,gender,salary,skills,department):
        super().__init__(name,age,gender,salary,skills)

        self.department = department

    def update(self):

        self.display_employee()
        print("Employee Department: ", self.department)

print("************ Added 'department' values using Inheritance concept")
print("")

dp = Department("Vijay", 41, "Male", 1000000, ["Functional-NonFunctional-Security Automation", "Python", "JS", "TS", "AI LLM"], "IT")
dp.update()

print("")

dp1 = Department("Deepthi", 40, "Female", 900000, ["BDS", "MDS"], "Dental")
dp1.update()

print("")

