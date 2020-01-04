
#Apko ek number diya jayega manlo x toh apko 1 se leke x ke bich meh joh bi number 3 or 5 se divisible hai ushe print kardo.

# number=int(input("Enter your choice no "))

# a=0
# while a<number:
# 	if a%3==0 or a%5==0:
# 		print(a)
# 	a+=1


###################################################################################################################################

'''Apko ish task meh koi bi ek number diya jayega uske piche ke 3 even number nikalo.
Jab yeh nikal jaye toh uske aage ke 3 odd number nikalo.'''

# no=int(input('Enter a range of choice'))
# number=int(input('Enter a choice number '))

# a=0
# var=1
# new_number=number
# while a<=var*no:
# 	if number%2==0:
# 		r=1
# 		print(r,'st previos no :',number)
# 		number-=2
# 	else:
# 		number+=1

# 	if new_number%2!=0:
# 		g=1
# 		new_number+=2
# 		print(g,'st Ahead of no ',new_number)
# 	else:
# 		new_number+=1
# 	a+=1


####################################################################################

# Write a program of leap year and find three leap year forward and three leap year of backward.

# year=int(input('Enter a leap Year: '))

# no=int(input('Enter no to find leap year: '))
# back_ward=[]
# forward=[]
# back_leap=year
# while True:

# 	year+=1
# 	back_leap-=1
# 	if year%4==0 and (year %400==0 or year %100!=0):
# 		if len(forward)==no:
# 			pass
# 		forward.append(year)
# 	if back_leap%4==0 and (back_leap%400==0 or back_leap%100!=0):
# 		if len(back_ward)==no:
# 			pass
# 		back_ward.append(back_leap)
# 	if len(back_ward)==no and len(forward)==no:
# 		break

# print('pichle teen no: ',end='')
# for i in forward:
# 	print(i,end=',')
# print('')
# print('aage ke teen leap year: ',end='')
# for i in back_ward:
# 	print(i,end=',')
# print('')


########################################################################################

# Amar Exercise question no 3 Armstrong No.

# user_input=int(input('Enter a user: '))

# for i in range(user_input):
# 	str_covert=str(i)
# 	sum1=0
# 	for j in range(len(str_covert)):
# 		r=i%10
# 		i=i//10
# 		sum1+=r**len(str_covert)
# 	if sum1==int(str_covert):
# 		print(str_covert)


####################################################################################

# user_input=int(input('Enter a user: '))

# for i in range(1,user_input):
# 	sum1=0
# 	for j in range(1,i//2+1):
# 		if i%j==0:
# 			sum1+=j
# 	if sum1==i:
# 		print(i)



#########################################################################


'''Apko ek string di jayegi jahan apko string ke phele 2 aur akhir ke 2 letters print karwana hai lekin agar woh string meh 2 se kaam letters hai toh kuch bi nhi print hoga.

'''


# user_input=input('Enter any string: ')

# if len(user_input)>=2:
# 	length=len(user_input)
# 	print(user_input[0:2]+user_input[length-2]+user_input[length-1])
# else:
# 	print('Empty')


#############################################################################

'''Question
Apko ek string di jayegi jiske akhir me agar 'ing' hogi toh ushe aage apko 'ly' add karni hai aur agar 'ing' nhi hai toh 'ing' add karna hai.
Lekin agar uske akhir meh 'ly' hai toh ushme app kuch bi add ni karoge

'''


# user_input=input('Enter any String: ')

# flag=len(user_input)
# rem=''
# i=0
# while i<flag:
# 	if user_input[i]=='i' and user_input[flag-2]=='n' and user_input[flag-1]=='g':
# 		rem=user_input
# 		rem+='ly'
# 		break
# 	elif user_input[i]=='l' and user_input[flag-1]=='y':
# 		rem=user_input
# 		break
# 	else:
# 		rem+=user_input[i]
# 	i+=1
# else:
# 	rem+='ing'
# print(rem)




###########################################################################

'''Apko ek string di jayegi jiske akhir me agar 'ing' hogi toh ushe aage apko 'ly' add karni hai aur agar 'ing' nhi hai toh 'ing' add karna hai.
Lekin agar uske akhir meh 'ly' hai toh ushme app kuch bi add ni karoge'''


# user_input=input('Enter any String: ')

# flag=len(user_input)
# rem=''
# i=0
# while i<flag:
# 	if user_input[i]=='i' and user_input[flag-2]=='n' and user_input[flag-1]=='g':
# 		rem+='ly'
# 		break
# 	elif user_input[i]=='l' and user_input[flag-1]=='y':
# 		rem=user_input
# 		break
# 	else:
# 		rem+=user_input[i]
# 	i+=1
# else:
# 	rem+='ing'
# print(rem)


########################################################################################

'''Apko ek postion di jayegi jish position tak ke sare Fibonacci series meh se 
jitne bi even number wale ha element hai uneh print karwana hai apko.'''

# user_input=int(input('Enter a range of Fibonacci series:  '))

# j=1
# i=0
# k=0
# new=[]
# while i<user_input:
# 	new.append(k)
# 	temp=k
# 	k=j+k
# 	j=temp		
# 	i+=1
# for i in new:
# 	if i%2==0:
# 		print(i)


#######################################################################################
'''
Question
Apko ek value di jayegi jese 10 toh apko 1-10 ke bich meh jitne bi number hai unke square ka sum nikalna hai aur uske baad 1-10 ke bich jitne number hai uske sum karke joh value aye uska square nikalna hai aur
dusri value meh se pheli value gatani hai.

1<sup>2</sup>+2<sup>2</sup>+3<sup>2</sup>+4<sup>2</sup>+.....+10<sup>2</sup> = 385'''


# user_input=int(input('Enter a no: '))

# squNum=0
# sum1=0
# for i in range(user_input+1):
# 	squNum+=i**2
# 	sum1+=i
# 	print(squNum)
# print((sum1*sum1)-squNum)



###############################################################################################

'''Apko ek number diya jayega aur apko ush number ke digit ke factorial ka sum nikalna hai.
Jese 2345 diya gaya hai apko toh iska factorial sum hoga.'''

user_input=int(input('Enter a no: '))
sum1=0
for i in range(len(str(user_input))):
	r=user_input%10
	user_input=user_input//10
	multi=1
	for j in range(1,r+1):
		multi*=j
	sum1+=multi
print(sum1)