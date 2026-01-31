
sub1 = int(input("enter the subject 1 number:"))
sub2 = int(input("enter the subject 2 number:"))
sub3 = int(input("enter the subject 3 number:"))

if(sub1>=33):
    print("subject 1 passed")
else:
    print("subject 1 failed")
if(sub2>=33):
    print("subject 2 passed")
else:
    print("subject 2 failed")
if(sub3>=33):
    print("subject 3 passed")
else:
    print("subject 3 failed")            

total = sub1+sub2+sub3    
print("total marks are:",total)
max_marks = 300
percentage = (total/max_marks)*100
print("percentage is:",percentage)

if(percentage<=40):
    print("failed")

else:
    print("passed")    


#this is short version of above program

#total_percentage = (100*(sub1+sub2+sub3))/ 300
#if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    #print("You are passed:",total_percentage)
#else:
    #print("better luck next time", total_percentage)    