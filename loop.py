	
#Ek program banao jo 1 se 100 tak ke saare numbers print karta hai.

# a=1
# while a<=100:
# 	print(a)
# 	a+=1
################################################################################################


#Ek program banao jo 1 se 100 tak ke beech mein woh numbers print kare jo 7 se divide ho jaate hain.

# a=1
# while a<=100:
# 	if (a%7==0):
# 		print(a)
# 	a+=1
# 	
#####################################################################################################

#Ek program likho jo loop ka use kar ke 1 se leke 100 tak saare numbers ka sum print kare.

# a=1
# sum=0
# while a<=100:
# 	sum+=a
# 	print(sum)
# 	a+=1

################################################################################################

# Ek loop banao jo user se 10 numbers ko input le. Input lene ke baad unn saare numbers ka sum print kare.

# a=1 
# sum=0
# while a<=10:
# 	number=int(input())
# 	sum+=number
	
# 	a+=1
# print(sum)	

#######################################################################################################3

'''Loop ka use kar ke yeh pattern print karo.

1, -2, 3, -4, 5, -6 …99, -100'''


# a=1
# while a<=100:
# 	if a%2==0:
# 		print(-1*a)
# 	else:
# 		print(a)
# 	a+=1	


#########################################################################################################

'''Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare:

Jo 3 se divisible hain unki jagah “Nav” print kare
Jo 7 se divisible hain unki jagah “Gurukul” print kare
Jo 3 aur 7 dono se divisible hain, unki jagah “NavGurukul” print karein
Jo upar wale teen cases mein nahi aate, unki jagah sirf number print karvao.'''

# a=1
# while a<=100:
# 	if a%3==0 and a%7==0:
# 		print('NavGurukul')
# 	elif a%7==0:
# 		print('Gurukul')
# 	elif a%3==0:
# 		print('Nav')
# 	else:
# 		print(a)
# 	a+=1

##################################################################################################

# Prime numbers woh numbers hote hai jo sirf 1 aur apne aap se divisible hote hain. Jaise

# a=2
# b=2
# while a<=100:
# 	while b<a//2+1:
# 		if a%b==0:
# 			break
# 		b+=1
# 	else:
# 		print(a)
# 	a+=1

#############################################################################################

'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1'''

# a=5
# while a>=1:
# 	print(str(a)*5,)
# 	a-=1

###############################################################################################

# Write a program to find Armstrong Number.

# number=int(input("Enter a range to find Armstrong no "))
# a=1
# while a<=number:
# 	b=1
# 	new=a
# 	sum1=0
# 	length=len(str(a))
# 	while b<=int(length):
# 		r=new%10
# 		new=new//10
# 		sum1=sum1+r**length
# 		if(new<10):
# 			sum1=sum1+new**length
# 			break
# 		b+=1
# 	if a==sum1:
# 		print(a)
# 	a+=1


############################################################################################

# Write a program to find Perfect No.

# number=int(input("Enter a range to find Perfect No "))
# a=1

# while a<=number:
# 	sum=0
# 	b=1
# 	while b<=a//2:
# 		if a%b==0:
# 			sum+=b
# 		b+=1
# 	if sum==a:
# 		print(a, "is perfect no ")
# 	a+=1


##########################################################################################

# Write a program to find Strong no.

# number=int(input("Enter a range to find strong no "))

# a=1
# while a<=number:
# 	sum1=0
# 	b=1
# 	c=1
# 	new=a
# 	length=len(str(a))
# 	while b<=length:
# 		r=new%10
# 		new=new//10
# 		fact=1
# 		while c<=r:
# 			fact=fact*r
# 			r-=1
# 		sum1+=fact
# 		b+=1
# 	if a==sum1:
# 		print(a, "is strong No")
# 	a+=1

###############################################################################################

# Write a program to find Fibonnic Series.

# a=0
# m=1
# temp=0
# number=int(input("Enter a range"))

# while a<=number:
# 	no=temp
# 	temp=m+no
# 	m=no
# 	a+=1
# 	print(no)


# ##################################################################################################

# # Write a program to find Tribonnic No.

# # a=0
# # m=1
# # temp=0
# # no=0
# # re=0
# # number=int(input('Enter a Range '))

# # while a<=number:
# # 	no=temp
# # 	temp=re+no
# # 	re=m+no
# # 	m=no
# # 	a+=1
# # 	print(no)


# ###############################################################################################3

# #Take 10 integers from keyboard using loop and print their average value on the screen.

# # a=1
# # sum=0
# # while a<=10:
# # 	number=int(input("Enter a no: "))
# # 	sum+=number
# # 	a+=1
# # print('Average', sum/10)
	

# ##################################################################################################

# '''Print the following patterns using loop :
# a.
# *
# **
# ***
# ****
# b.
#    *  
#   *** 
#  *****
#   *** 
#    *  
# c.
# 1010101
#  10101 
#   101  
#    1   '''


# # a

# # a=1
# # while a<=5:
# # 	print('*'*a)
# # 	a+=1

# # b
# # i = 1
# # j = 2
# # while i>=1:
# #   a =  " "*j+"*"*i+" "*j
# #   print (a)
# #   i = i+2
# #   j = j-1
# #   if i>5:
# #     break
# # i = 3
# # j = 1
# # while i>=1:
# #   a =  " "*j+"*"*i+" "*j
# #   print (a)
# #   i = i-2
# #   j = j+1
# #   


# # c

# # i=3
# # j=0

# # while i>=0:
# # 	a=" "*j+'10'*i+'1'+' '*j
# # 	print (a)
# # 	i=i-1
# # 	j=j+1

# ##########################################################################################################

# #Print multiplication table of 24, 50 and 29 using loop.

# # a=1

# # while a<=10:
# # 	print(24*a,'\t', 50*a,'\t', 29*a,'\t')
# # 	a+=1 

# ##########################################################################################

# # Write a program to find a HCF Number.

# # first_number=int(input("Enter a first_number: "))
# # second_number=int(input("Enter a Second number: "))

# # a=1
# # hcf_no=0
# # while a<first_number:
# # 	if first_number%a==0 and second_number%a==0:
# # 		hcf_no=a
# # 	a+=1
# # print(hcf_no)

# ################################################################################################

# '''Calculate the sum of digits of a number given by user. E.g.-
# INUPT : 123        OUPUT : 6
# INUPT : 12345        OUPUT : 15'''

# # number=int(input('Enter a number'))

# # a=1
# # length=len(str(number))
# # sum=0
# # while a<=length:
# # 	r=number%10
# # 	number=number//10
# # 	sum+=r
# # 	a+=1
# # print(sum)


# ###############################################################################################

# '''Write a program to print a number given by user but digits reversed. E.g.-
# INPUT : 123        OUTPUT : 321
# INPUT : 12345        OUTPUT : 54321'''

# # number=int(input('Enter a number: '))

# # a=1
# # length=len(str(number))
# # sum=''
# # while a<=length:
# # 	r=number%10
# # 	number=number//10
# # 	sum+=str(r)
# # 	a+=1
# # print(sum)

# ##############################################################################################

# # Write a program to find length from of a list.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7,8]

# new=[]
# count=0
# a=0
# while True: 
# 	if numbers==[]:
# 		print(count)
# 		break
# 	else:
# 		numbers.remove(numbers[a])
# 		count+=1


################################################################################################

'''Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. Aur firr unka count print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]'''

# number=[50, 40,25,36,28, 23, 70, 56, 12, 5, 10, 7]

# legth=len(number)

# a=0
# count=0
# while a<legth:
# 	if 20<number[a]<40:
# 		count+=1
# 		print(number[a])
# 	a+=1
# print(count)

#################################################################################################

'''Code likho jo iss list mein se maximum dhund kar ke print kare.'''

# numbers = [50, 40, 230, 70, 56, 12, 5, 10, 7]

# great=0
# a=0
# while a<len(numbers):
# 	if numbers[a]>great:
# 		great=numbers[a]
# 	a+=1
# print("Greatest number of that list is: ",great)

#############################################################################################

'''Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.'''

# numbers = [50, 400, 23, 70, 56, 12, 5, 10, 7]

# great=0
# sec_great=0
# a=0
# b=0
# while a<len(numbers):
# 	if numbers[a]>great:
# 		great=numbers[a]
# 	a+=1
# while b<len(numbers):
# 	if numbers[b]>sec_great and numbers[b]<great:
# 		sec_great=numbers[b]
# 	b+=1
# print('Frist Gretest Number: ',great)
# print('Second Greatest Number: ',sec_great)

#####################################################################################################

# Write a programe to find a no is palindrome and not.

# Char=input('Enter a word : ')
# length=len(Char)

# a=1
# sum=''
# while a<=length:

# 	sum=sum+Char[a*-1]
# 	print(sum)
# 	a+=1
# if sum==Char:
# 	print('It is a palindrome')
# else:
# 	print('It is not a palindrome')
# 	

####################################################################################################

# Write a program to convert a binary number to Decimal no.

# Binary_list=[]

# no=int(input('Enter a range of Binary no: '))
# a=1
# while a<=no:
# 	number=int(input('Enter a binary number: '))
# 	Binary_list.append(number)
# 	a+=1
# # now converted into decimal no
# b=0
# sum=0
# c=2
# while b<no:
# 	sum+=Binary_list[b]*(c**b)
# 	print(sum)
# 	b+=1


########################################################################################################

'''Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.'''

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]

# list3=[]
# length=len(list1)
# a=0
# while a<length:
# 	if list1[a] not in list2:
# 		list3.append(list1[a]) 
# 	a+=1
# print(list3)


###################################################################################################

''' write a program to find sum of total list 
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]'''


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]

# a=0
# sum=0
# while a<len(marks):
# 	b=0
# 	while b<len(marks[a]):
# 		sum=sum+marks[a][b]
# 		b+=1
# 	a+=1
# print(sum)

# #############################################################################################################

# ''': How to find all pairs in an array of integers whose sum is equal to the given number?

# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]'''


# n = [10, 11, 12, 13, 14, 17, 18, 19]

# print([n[0],n[2]])


###############################################################################################################

# Write a program to sort a list with using one loop only.


# list1=[1,5,8,52,6,9,41,5]
# i=0

# while i<(len(list1)-1):
# 	if list1[i]<=list1[i+1]:
# 		a=1
# 	else:
# 		temp=list1[i]
# 		list1[i]=list1[i+1]
# 		list1[i+1]=temp
# 		i=0
# 	i+=1
# print(list1)
