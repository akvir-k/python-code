
#Take values of length and breadth of a rectangle from user and check if it is square or not.

# print("Enter a length value")
# length=int(input())
# print("Enter a breadth value")
# breadth=int(input())
# if(length==breadth):
# 	print("It is a square")
# else:
# 	print('It is not a square')


###################################################################################################

#Take two int values from user and print greatest among them.

# no=int(input("Enter a first no "))
# no2=int(input("Enter a Second no "))

# if no<no2:
# 	print("Second no is greater ", no2)
# else:
# 	print("First no is greater ",no)

#################################################################################################
'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''

# quantity=int(input("Enter a purchased quantity: "))

# if (quantity<=1000):
# 	print("No discount because discount available after 1000 purchased")
# else:
# 	discount=quantity*10/100
# 	print("Your net price is : ",quantity-discount)

######################################################################################################
'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''

# salary=int(input("Enter a employee salary: "))
# service_year=int(input("Enter a Employee service year: "))

# if service_year>5:
# 	print("Salary with bonus",(salary+(salary*5/100)))
# else:
# 	print("only salary no bonus: ", salary)

####################################################################################################
'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

# Student_marks= int(input("Enter a Student_marks: "))

# if Student_marks>80:
# 	print(" Student grade is 'A'")
# elif 60<=Student_marks<=80:
# 	print("Students grade is 'B'")
# elif 50<=Student_marks<60:
# 	print("Student grade is 'C'")
# elif 45<=Student_marks<50:
# 	print("Student grade is 'D'")
# elif 25<=Student_marks<45:
# 	print( "Student grade is 'E'")
# elif 0<=Student_marks<25:
# 	print("Students grade is 'F'")
# else:
# 	print("error input")

####################################################################################################

# Take input of age of 3 people by user and determine oldest and youngest among them.

# first_people=int(input("Enter first person age: "))
# second_people=int(input("Enter second person age: "))
# third_people=int(input("Enter third person age: "))

# if first_people>second_people:
# 	if(first_people>third_people):
# 		print("oldest people is first one")
# 	else:
# 		print("oldest people is third one")
# elif second_people>third_people:
# 	print("oldest people is second one")
# else:
# 	print("oldest people is third one")

# if first_people<second_people:
# 	if first_people<third_people:
# 		print("youngest people is first person ")
# 	else:
# 		print("yongest people is third person")
# elif second_people<third_people:
# 	print("yongest people is second person ")
# else:
# 	print("yongest people is third person")

#################################################################################################

'''Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1'''


# number=int(input("Enter a number:"))

# if number<0:
# 	print("abolute no is ",-1*number)
# else:
# 	print("absolute no is ",number)


##############################################################################################
'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.'''

# class_held=int(input('Enter the no of classes'))
# class_attend=int(input('Enter the no of class attend '))

# percentage_of_attendance=class_attend*100/class_held

# if percentage_of_attendance>70:
# 	print("you are eligible for give to his exam",percentage_of_attendance)
# else:
# 	print('you are not eligible',percentage_of_attendance)



############################################################################################

# write a program to check year is leap year or not.

# year=int(input("Enter a year"))

# if year%4==0 and (year%400 ==0 or year %100!=0):
# 	print("It is a leap year")
# else:
# 	print("It is not a leap year ")


#############################################################################################

''' Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".'''


# sex=input("Enter sex of employee: M:Male, F:Female")
# age=int(input("enter a age of employee"))
# marital_status=input('Enter the marital status of employee: Y:yes and N:No')

# if sex=='F':
# 	print('Employee is female , the she will work only in urban areas')
# else:
# 	if 20<age<40:
# 		print('He may work in anywhere')
# 	elif 40<age<60:
# 		print('He will work in urban areas only')
# 	else:
# 		print("error age input")		


###########################################################################################

'''A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895'''

# number=int(input('Enter a number '))

# First_no=number//1000
# rem=number%1000

# second_number=rem//100
# rem=number%100

# third_number=rem//10
# rem=number%10

# print('reversed no is ', (rem*1000)+(third_number*100)+(second_number*10)+First_no)

#############################################################################################


user=input('Enter a anything:')


if type(user)==int:
	print('Integer')
else:
	if type(int(user))== int:
		print('Integer')
	else:
		user=float(user)
		if type(user)==float:
			print('Float')
		else:
			print('string')
