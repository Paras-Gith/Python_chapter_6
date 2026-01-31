# 01 WAP to display the last digit of a number. (Don’t use indexing for this) 
# #num = int(input("Enter a numbner: "))
# if num < 10:
#     print(num)
# else:
#     last = num % 10
#     print(last)


# 02 WAP to check if a single character is a vowel or not

# char = input("Enter the character: ").lower()
# if (char in "aeiou"):
#     print("this a vowel")
# else:
#     print("enter the vowel")

# 03 WAP to check if a number is even or odd where the number is taken as input.
# num = int(input("Enter the number:"))
# if num % 2 == 0 :
#     print("the number is even")
# else:
#     print("the number is odd")

# 04 WAP to check if the 3rd last character of a string is a vowel or not.

# word = input("enter a word: ").lower()
# if len(word) <= 2:
#     print("length is too small")
# else:
#     ch = word[-3]
#     if ch in "aeiou":
#         print("the 3rd character is a vowel")
#     else:
#         print("the 3rd character is not a vowel")    

# 05 Check if the first and last number of a list is same or not. Take a pre-defined list in the code itself.

# numbers = [1, 7, 0, 25, 44, 99, 1]
# if numbers[0] == numbers[-1]:
#     print("the number is first and last number are same")
# else:
#     print("the number first and last are not same")    

# 06 Calculate income tax for the input income by adhering to the Indian rules.

# income = int(input("Enter the your income: "))

# if (income <= 300000):
#     print("Nill")
# elif (300001 <= income <= 700000):
#     print("Nill(due to rebate u/s 87A if total income ≤ 7L)")    
# elif (income in range(700001, 1000000)):
#     taxable_income = (income - 700000)
#     tax  = float(0.1 * taxable_income)
#     print("your taxable income is: ", tax)
# elif (income in range(1000001, 1200000 + 1)):
#     taxable_income = (income - 1000000)
#     tax = float(0.1 * (1000000 - 700000))
#     tax += float(0.15 * taxable_income)
#     print("your taxable income is: ", tax)     
# elif (income in range(1200001, 1500000 + 1 )):
#     taxable_income = (income - 1200000)
#     tax = float(0.1 * (1000000 - 700000))   # 7–10L
#     tax += float(0.15 * (1200000 - 1000000))
#     tax += float(0.2 * taxable_income)
#     print("your taxable income is: ", tax)
# elif (income > 1500000):
#     taxable_income = (income - 1500000)
#     tax = float(0.1 * (1000000 - 700000))   # 7–10L
#     tax += float(0.15 * (1200000 - 1000000)) # 10–12L
#     tax += float(0.2 * (1500000 - 1200000))
#     tax += float(0.3 * taxable_income)
#     print("your taxable income is: ", tax)  
# else:
#     print("error")


# 07 Write a Python program to check whether a string starts with vowel or not.

# ch = input("Enter the string: ").lower()
# if ch[0] in "aeiou":
#     print("the string starts with vowel")
# else:
#     print("the string do not start with vowel")     

# 08 WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user. Using percentage print which grade the student has scored.

# subject_1 = int(input("enter the marks: "))
# subject_2 = int(input("enter the marks: "))
# subject_3 = int(input("enter the marks: "))
# subject_4 = int(input("enter the marks: "))
# subject_5 = int(input("enter the marks: "))

# total_of_subjects = (subject_1 + subject_2 + subject_3 + subject_4 + subject_5)
# print("the total of subjects: ",total_of_subjects)

# percentage = (total_of_subjects / 500) * 100
# print("the percentage of the student:" ,percentage)

# if percentage >=91:
#     print("grade A1")
# elif percentage >=81:
#     print("grade A2")
# elif percentage >=71:
#     print("grade B1")
# elif percentage >=61:
#     print("grade B2")
# elif percentage >=51:
#     print("grade C1")
# elif percentage >=41:
#     print("grade C2")                    
# elif percentage >=33:
#     print("grade D")    
# else:
#     print("fail")    
    

# 09 WAP to convert a celsius value to fahrenheit. Take celsius value as input.

# temp = float(input("enter the valuse in celsisus: "))
# fahrenheit = ((9/5)*temp) + 32
# print("the value in fahrentheit is: ", fahrenheit)


# 10 WAP to calculate the surface area of a triangle. Take the length of sides as input.


# a = float(input("enter the side: "))
# b = float(input("enter the side: "))
# c = float(input("enter the side: "))

# if a + b > c and a + c >b and c + b >a:
#     s = (a + b + c)/2
#     area = (s * (s - a) * (s - b) * (s - c))**(1/2)
#     print(f"Surface area of Triangle is : {area}")
# else:
#     print("Invalid triangle sides!")


# 11 WAP to print the day based on the number input.For example: if input = 1, output = Monday

# This is mine written code but have worst time complexity

# num = int(input("enter the number"))
# if num > 7:
#     print("invalid")
# else:
#     if num == 1 :
#         print("Monday")
#     elif num == 2 :
#         print("Tuesday")
#     elif num == 3:
#         print("Wednesday")
#     elif num == 4 :
#         print("Thrusday")
#     elif num == 5 :
#         print("Friday")
#     elif num == 6 :
#         print("Saturday")
#     elif num == 7:
#         print("Sunday")
#     else:
#         print("invalid")                       

# OR this one is using dict

# d = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thrusday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

# num = int(input("enter the numner: "))
# if num<=7 and num >= 1:
#     print(d[num])
# else:
#     (print("invalid"))


# 12 WAP to check whether a person is eligible to vote or not based on their age.

# Age = int(input("enter the AGE: "))
# if Age >= 18:
#     print("eligible to vote")
# else: 
#     print("Not Eligible to vote")    


# 13 WAP to calculate the count of elements in a string.

# s = input("enter the string: ")
# count = len(s)
# print("the count of string: ", count)


# 14 WAP to check using the sides of a triangle to tell if it is equilateral triangle or not.

# a = float(input("enter the side: "))
# b = float(input("enter the side: "))
# c = float(input("enter the side: "))

# if a == b == c:
#     print("the triangle is equilateral triangle")
# else :
#     print("the triangle is not equilateral triangle")    



# 15 WAP to check if the 2nd last digit of numerical input from the user is divisible by 3 or not.

# num = int(input("enter the numerical value: "))
# num_str = str(num)
# second_last = int(num_str[-2])
# if len(num_str) <2 :
#     print("too short.")
# else:
#     second_last = int(num_str[-2])
#     if second_last % 3 == 0 :
#         print("it is divisible by 3")  
#     else :
#         print("it is not divisible by 3")

# 16 Write a Python program that takes two numbers as input from the user and prints the larger of the two numbers.

# num_1  = int(input("enter the number: "))
# num_2 = int(input("enter the number: "))
# if num_1 > num_2 :
#     print("num_1 is larger")
# elif num_2 > num_1:
#     print("The larger number is:", num_2)
# else:
#     print("Both numbers are equal.")


