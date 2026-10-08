# To create a Developer class and assign some values by using the object.

class Developer:

    name : str
    id : int
    email : str
    title : str
    level : str
    salary : float
    skills : list

    def __init__(self, name, id, email, title, level, salary, skills):

        self.name = name
        self.id = id
        self.email = email
        self.title = title
        self.level = level
        self.salary = salary
        self.skills = skills

    def display_developer(self):

        print("Developer Name: ", self.name)
        print("Developer id: ", self.id)
        print("Developer email: ", self.email)
        print("Developer title: ", self.title)
        print("Developer level: ", self.level)
        print("Developer salary: ", self.salary)
        print("Developer skills: ", self.skills)

print("")

dev = Developer("Junjuri", 3777, "abc@gmail.com", "Assosiate Director", "A", 1100000, ["Automation", "JS", "TS", "Python", "AI LLM"])
dev.display_developer()

print("")

dev1 = Developer("Katuri", 3888, "def@gmail.com", "Assosiate Surgen", "B", 900000, ["BDS", "MDS"])
dev1.display_developer()

print("")



# Inheritance
#creating a child class to inherit properties & methods from Employee(parent) class


class Department(Developer):

    department : str

    def __init__(self, name, id, email, title, level, salary, skills,department):
        super().__init__(name, id, email, title, level, salary, skills)

        self.department = department

    def update(self):

            self.display_developer()
            print("Developer Department: ", self.department)


print("************ Added 'department' values using Inheritance concept")
print("")

dev2 = Department("Junjuri", 3777, "abc@gmail.com", "Assosiate Director", "A", 1100000, ["Automation", "JS", "TS", "Python", "AI LLM"], "IT")
dev2.update()

print("")

dev3 = Department("Katuri", 3888, "def@gmail.com", "Assosiate Surgen", "B", 900000, ["BDS", "MDS"], "Dental")
dev3.update()

print("")

