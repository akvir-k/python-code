
# this_dict={
# 			"brand":'Ford',
# 			"model":'Mutang',
# 			"year": 1964
# }
# print(this_dict)

# ####
# # Access items

# x=this_dict['model']
# print(x)

# ## Access items with get method

# x=this_dict.get('model')
# print(x)

# ###########
# # Change value in dictionary

# this_dict['year']=2019
# print(this_dict)

# ########
# # using loop in dictionary

# for x in this_dict:
# 	print(x)			# when we can acces by loop so its return only key.


# ############
# # Access value in loop

# for x in this_dict.values():
# 	print(x)

# ##########
# # If we access both key and values at a time so we can use 'items funtion'.

# for x , y in this_dict.items():
# 	print(x,y)

# ############
# # check it if key exit in dictonary

# if 'model' in this_dict:
# 	print('model')

# ###########

# # add key and values in dictonary.

# this_dict['color']='red'
# print(this_dict)

# #############
# # removing items in dicitonary
# # using pop() method;

# this_dict.pop('model')
# print(this_dict)

# #### 
# popitems()

# this_dict.popitem()
# print(this_dict)

###########
# Del removed a items with specificd name.

# del this_dict['brand']
# print(this_dict)

############
# clear() this keyword empties all dictionary.

# this_dict.clear()
# print(this_dict)


###############################################################
# Nested Dictionary.

# family={
# 		"child1":{"name":"Roshan","year":2004},
# 		"child2":{"name":"Prabhakar","year":2009},
# 		"child3":{"name":"Himani","year":1993},
# }
 # print(family)

########
# Access items in nested Dictionary.


###################################################################################

# Write a program to print a roman no in with help of dictionary.

# roman_no={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

# user_input=int(input("Enter a number for convert into roman No: "))
# sum=''
# for i in roman_no:
# 		r=user_input//i
# 		user_input=user_input%i
# 		sum=sum+roman_no[i]*r
# print(sum)


####################################################################################

# # Write a program to board mass funtion with help of dictionary.						
# import string
# new=[]
# add=''
# rem=''
# k=0
# numList=input("Enter a no: ")
# for i in range(len(numList)):
# 	# if numList[i] in string.punctuation and numList[i+1]==numList[i]:
# 	# 	pass
# 	if numList[i] in string.punctuation and k==1:
# 		rem+=numList[i]
# 		new.append(int(add))
# 		new.append(rem)
# 		add=''
# 		rem=''
# 		k=0
# 	else:
# 		add+=numList[i]
# 		k=1
# new.append(int(add))
# print(new)

# while True:
# 	index=0
# 	calc=0
# 	if '/' in new:
# 		index=new.index('/')
# 		calc=new[index-1]/new[index+1]
# 	elif '*' in new:
# 		index=new.index('*')
# 		calc=new[index-1]*new[index+1]
# 	elif '+' in new:
# 		index=new.index('+')
# 		calc=new[index-1]+new[index+1]
# 	elif '-' in new:
# 		index=new.index('-')
# 		calc=new[index-1]-new[index+1]

# 	del new[index-1:index+2]
# 	new.insert(index-1,calc)
# 	if len(new)==1:
# 		break
# print(new)

###############################################################################

# Write a program to convert word to numercal no.

# word={'Thousand':1000,'Hundred':100,"Ninty":90,"Eight":80,'Seventy':70,'Sixty':60,
# 		'Fifty':50,'Forty':40,'Thirty':30,'Twenty':20,'Ten':10,'Nine':9,'Eight':8,'Seven':7,'Six':6,
# 		'Five':5,'Four':4,'Three':3,'Two':2,'One':1
# 		}
# No=input('Enter no in word')
# new=No.split()
# list1=[]
# list2=[]
# sum=0
# for i in new:
# 	if i=='Thousand' or  i=='Hundred':
# 		list1.append(word[i])
# 	else:
# 		list2.append(word[i])

# for i in range(len(list1)):
# 	if list1[i]==1000 or list1[i]==100:
# 		sum=sum+list1[i]*list2[i]
# 		list2.pop(i)
# 		list2.insert(i,0)
# for j in list2:
# 	sum+=j
# print(sum)


########################################################################################

# Write a program to remove zero after decimal value fi continues zero come.

# Number=input('Enter a Decimal No:')
# no=float(Number)
# b=no-int(no)
# print(b)

################################################################################

# Write a program to print table and store in dictionary.


# user_input=int(input('Enter a no by user: '))
# dict1={}
# for i in range (1,user_input+1):
# 	new=[]
# 	mult=0
# 	for j in range(1,10+1):
# 		mult=i*j
# 		new.append(mult)
	
# 	dict1[i]=new
# print(dict1)
 
#####################################################################################
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
Actions
 '''


# i=100
# big=0
# first_value,mulitple_value,second_value=0,0,0
# while i<1000:
# 	j=100
# 	while j<1000:
# 		pro=str(i*j)
# 		# print(pro)
# 		rev=pro[::-1]
# 		# print(i,j,rev,pro)
# 		if pro==rev:
# 			if int(pro)>big:
# 				big=int(pro)
# 				first_value=i
# 				second_value=j		
# 		j+=1
# 	i+=1
# print(first_value,'x',second_value,big)



number=int(input('enter a no'))

i=2
new=[]
str_number=str(number)
if int(str_number[-1])%2==0:
	i=2
else:
	i=3
while i<=number//2+1:
	if number%i==0:
		new.append(i)
		print(new)	
	i+=2
print(new)
for i in new:
	j=2
	while j<=i//2+1:
		if i%j==0:
			break
		else:
			j+=1
	else:
		print(i)


