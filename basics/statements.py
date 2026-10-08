#Conditional Statements

#If Statement

age=18

if (age>=18):
    print("You are eligible for voting")


#If else statement

if (age>=18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


#If elif else statement

metrics = "Hallucination"

if metrics == "Hallucination":
    print("Execute Hallucination test")

elif metrics =="Bias":
    print("Execute Bias test case")

elif metrics == "Security":
    print("Execute Red Teaming testing")

else:
    print("Execute Web Application Testing")



#Match-Case statement

metricsName = "Security"

match metricsName:
    case "Hallucination":
        print("Execute Hallucination test")

    case "Bias":
        print("Execute Bias test")

    case "Safety":
        print("Execute Safety test")

    case _:
        print("Execute Web Application Testing")



#Assignment
#Write a program to define the grading system:

#Using if elif statement
#-----------------------

marks = 97

if (marks > 90 and marks <=100):
    print("The student atained Grade A")

elif (marks > 80 and marks <=90):
    print("The student atained Grade B")

elif (marks > 70 and marks <=80):
    print("The student atained Grade C")

elif (marks < 70 and marks >=0):
    print("The student atained Grade D")

else:
    print("The student marks are Invalid")


#Using Match-Case statement
#-----------------------

marks1 = 75

match marks1:

    case marks1 if (marks1 > 90 and marks1 <=100):
        print("The student atained Grade A")

    case marks1 if (marks1 > 80 and marks1 <=90):
        print("The student atained Grade B")

    case marks1 if (marks1 > 70 and marks1 <=80):
        print("The student atained Grade C")

    case marks1 if (marks1 < 70 and marks1 >=0):
        print("The student atained Grade D")

    case _:
        print("The student marks are Invalid")