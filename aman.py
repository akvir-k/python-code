# day=input("enter the day")
# time=input("enter the time ")
# if day=="monday" and time=="morning":
# 	print("monday ko morning main milk and chidva")
# elif day=="monday" and time=="afternoon":
# 	print("monday ko lunch main dal roti milega")
# elif day=="monday" and time=="evening":
# 	print("sabji or roti")
# elif day=="tuesday" and time=="morning":
# 	print("kheer and chawwal")
# elif day=="tuesday" and time=="afternoon":
# 	print("bhujiya and parantha")
# elif day=="tuesday" and time=="evening":
# 	print("dal or roti")


# bredth=int(input("enter the no"))
# lenth=int(input("enter the no"))
# if bredth>lenth:
# 	print('square is possible')
# else:
# 	print('square is not possible')




# unit=int(input("enter the consumer uni"))
# if(unit>1000):
# 	print("discount applicable")
# 	print("Total cost of consumer "+str(unit-(unit*10/100)))
# else:
# 	print("discount not applicable")




# salary=int(input("enter the salary"))
# services=int(input("enter the year of services"))
# if(services>5):
# 	print("Employee net bonus "+str(salary*5/100))
# else:
# 	print("no bonus")
# 	

# marks=int(input("enter the students marks "))
# if(marks<25):
# 	print('f grade')
# elif 25<=marks<45:
# 	print('E grade')
# elif 45<=marks<50:
# 	print('D grade')
# elif 50<=marks<60:
# 	print('C grade')
# elif 60<=marks<80:
# 	print('B grade')
# elif marks>=80:
# 	print('A grade')


# 	

# print('enter the age')
# first_age=input()
# second_age=input()
# third_age=input()
# if(first_age>second_age and first_age>third_age):
# 	print("oldest age")
# elif second_age>third_age and second_age>first_age:
# 	print("second is oldest")
# elif third_age>first_age and third_age>second_age:
# 	print("third age is oldest")
# else:
# 	print('all equal')
# 	



# total_class=input("enterr the total class ")
# attend_class=input('enter the class attend')
# medical=input('enter the medical details')
# print('total class '+total_class)
# print('total attend class '+attend_class)
# percentage=int(attend_class)*100/int(total_class)
# print("percentage of attendance "+str(percentage))
# if percentage>70  and medical=="yes" :
# 	print('eligible for exam')
# else:
# # 	print('not eligible for exam')
# # 	





# first=input("enter a alphabets and minmum 4 and maximum 8 charector")
# second=input("enter a 4 digit")
# third=input("enter a one special charector")
# combined=first+second+third
# print('strong password here = '+combined)
# password=input('enter a passowrd')
# if(combined==password):
# 	print("password match")
# # else:
# # 	print("password does not match")


# year=int(input('enter a year '))
# if(year%400==0 or year%4==0 and year%100!=0):
# 	print("yes it is a leap year")
# else:
# 	print('it is not a leap year')




# age=int(input('enter the age '))
# sex=input('enter the gender Male or Female  ')
# marrital_status=input('are you married and not! ')
# if(sex=="male" and 20<age<40 and marrital_status=="yes"):
# 	print('%d he may work in any where')
# elif(sex=="female" and marrital_status=="yes"):
# 	print('She will work only urban areas')
# elif(sex=="male" and 40<age<60 and marrital_status=="yes"):
# 	print("%d he will work at urban areas")
# else:
# 	print("error")







# digit=int(input('enter a digit'))
# if(digit<0):
# 	print('Negetive')
# elif digit==0:
# 	print('zero')
# else:
# # 	print('positive')

# digit=int(input('enter a digit'))
# if(digit%5==0 and digit%11==0):
# 	print('no is divisible by 5 and 11')
# else:
# 	print("no is not divisible by 5 and 11")






# a=5
# b=2

# temp=0
# temp=a
# a=b
# b=temp

# print(a)
# # print(b)


# age=int(input("age daalo"))
# if age>=5: 
# 	print("school ja  sakte ho")
# if age>=18:
#  	print ("vote daal sakte ho")
# if age>=21:
#  	print ("car drive kar sakte ho")
# if age>=24:
#  	print ("shaadi kar sakte ho")
# if age>=25:
#  	print ("legally drink kar sakte ho")

#  	



# i=0
# sum=0
# while i<=100:
# 	sum=sum+i
# 	# print(sum)
# 	i=i+1
# print(sum)


# i=1
# while i<100:
# 	print(i)
# 	i=i+1


# i=20
# while i<40:
# 	if i%2==0:
# 		print(i)
# 	else:
# 		print("not divisible")
# 	i=i+2



# sum=0
# no=0
# while no<5:
# 	h=int(input('enter the no '))
# 	no=no+1
# 	sum=sum+h
# print(sum)



# no=0
# while(no<100):
# 	if no%2==0:
# 		print(-1*no)
# 	else:
# 		print(no)
# 	no=no+1
# 		


#########################################################################
# print tribonic series

# no=0
# sum=0
# h=1
# m=0
# while no<=100:
# 	no=sum
# 	sum=no+m
# 	m=no+h
# 	h=no
# 	print(no)


# a=-1
# while a>=(-10):
# 	print(-a)
# 	a=a-1




# i=891
# while i<931:
# 	z=i-890
# 	if(z%3==0):
# 		print (z)
# 	i=i+1

# 	


# i=0
# while(i<50):
# 	i=i+5
# 	print(i)

# 	




# i=50
# sum=0
# while i<100:
# 	if(i%2==1):
# 		sum=sum+i
# 		print(i)
# 	i=i+1



# i=556
# while i<1000:
# 	s=i-555
# 	if(s%7==0):
# 		print(s)
# 	i=i+1
#################################################
# print prime no 2 to 100 with while loop

a=2
while a<100:
	i=2
	while i<a:
		if a%i==0:
			break
		i+=1
	else:
		print(a)
	a=a+1




# i=0
# while i<100:
# 	if (i%3==0 and i%7==0):
# 		print("Navgurukul")
# 	elif(i%3==0):
# 		print("Nav")
# 	elif i%7==0:
# 		print("gurukul")
# 	else:
# 		print(i)
# 	i=i+1

# 	




# i=50 
# sum=0
# while i<59:
# 	z=i-49
# 	f=int(input("enter the no here:) "))
# 	sum=sum+f
# 	print(sum)
# 	i=i+1


###############################################################
# PRINT THE PATTERN

# i=1
# while i<=5:
# 	print("*" *i)
# 	i=i+1

##############################
# ek no input lo user se baad me user utni hi barr input lega and uske baad unko add karo

	
# n=int(input("enter the no to input by the user"))
# i=1
# sum=0
# while i<=n:
# 	f=int(input("enter the value by the user"))
# 	sum=sum+f
# 	i+=1
# print(sum)



###########################################################
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1

# i=5
# while i>=1:
# 	print (str(i)*5)
# 	i=i-1


####################################################
#input 10 weight from user and print sum of all weight and find the avearge of the weight after the
# print and confirm it average is multiple of 5.


# i=0
# sum=0
# while i<10:
# 	h=int(input("enter the person weight "))
# 	sum=sum+h
# 	i=i+1
# print("Total person weight",sum)
# avg=sum/10
# print("average of weight", avg)
# if(avg%5==0):
# 	print("average is muliple of 5")
# else:
# 	print("average is not muliple of 5")


####################################################################################
# # guessing game code
# i=5
# f=1
# while f<=5:
# 	no=int(input("Enter the No"))
# 	if no==i:
# 		print("You are gussing a right ")
# 		break
# 	print("dubara guess karo")
# 	f=f+1	
# else:
# 	print("you have try 5 times now you can try next day")

# 	


###############################################################################
# # guessing game code and check the no is smaller and greater
# i=10
# f=1
# while f<=10:
# 	no=int(input("No guess karo"))
# 	if(no==i):
# 		print("wow! aapne guess kar liya")
# 		break
# 	if no<i :
# 		print("no is smaller from the guess no")
# 	if no>i:
# 		 print("no is greater from the guess no")
# 	print("dubara guess karo")
# 	f+=1
# else:
# 	print("you have tried 10 times now you can try 3 days later")




# counter=1
# while counter<10:
# 	if counter%2==0:
# 		print ("counterr ever numberr hai")
# 	print ("the counterr is"+str(counter))
# 	counter=counter+1
# print ('-------------------')



# ###############################################################
# # print factorial no
# no=int(input("enter a no"))
# f=1
# if no==0:
# 	print (1)
# else:
# 	while no>=1:
# 		f=f*no
# 		no-=1
# print(f) 




# f=5
# i=1
# while i<5:
# 	h=int(input("enter the no"))
# 	if(h==f):
# 		print('your guess is right')
# 		break
# 	print("dubara print kare")
# 	i=i+1
# else:
# 	print("enter wrong time")


#############################################################################
# print  Armstrong no


# no=int(input('enter a no'))	
# h=len(str(no))
# g=no
# s=0
# while no>0:
# 	m=no%10
# 	no=no//10
# 	s=s+(m**h)
# 	if(no<=1):
# 		s=s+no
# 		break
# print(s)
# if(s==g):
# 	print("No is a armstrong no")
# else:
# 	print("No is not a armstrong no")

	


# n=int(input('enter a no'))
# s=0
# while True:
# 	r=n%10
# 	n=n/10
# 	s=s+r
# 	if(n<10):
# 		s=s+n
# 		break
# print(s)




