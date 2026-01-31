student = int(input("enter the marks:"))

if(student<=100 and student>=90):
    grade = "Ex"
elif(student<=90 and student>=80):
    grade = "A"
elif(student<=80 and student>=70):
    grade = "B"
elif(student<=70 and student>=60):
    grade = "C"
elif(student<=60 and student>=50):
    grade = "D"
elif(student<50): 
    grade = "F"

print("Your grade is:", grade)    