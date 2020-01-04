# a=[1,2,[3],3,[12,3,4,5,[2,34,[4,5,[53,3,3,[333,3,3,3,]],[242,4,4,4,[44,4,44,[75,3,3,4,5,[786,[1],]]]]]]]
# # Q1. sum all digit 
# # Q2. find index of highest digit and  print also

# sum=0
# for i in a:
# 	if type(i)==list:
# 		for j in i:
# 			if type(j)==list:
# 				for k in j:
# 					if type(k)==list:
# 						for l in k:
# 							if type(l)==list:
# 								for m in l:
# 									if type(m)==list:
# 										for n in m:
# 											if type(n)==list:
# 												for o in n:
# 													if type(o)==list:
# 														for p in o:
# 															if type(p)==list:
# 																for q in p:
# 																	sum+=q
# 															else:
# 																sum+=p
# 													else:
# 														sum+=o
# 											else:
# 												sum+=n		
# 									else:
# 										sum+=m
# 							else:
# 								sum+=l
# 					else:
# 						sum+=k
# 			else:
# 				sum+=j
# 	else:
# 		sum+=i
# print(sum)							



#######################

# a=[1,2,[3],3,[12,3,4,5,[2,34,[4,5,[53,3,3,[333,3,3,3,[242,4,4,4,[44,4,44,[75,3,3,4,5,[786,[1]]]]]]]]]]] 
# # Q2. find index of highest digit and  print also
# index=0
# great=0
# for i in a:
# 	if type(i)==list:
# 		for j in i:
# 			if type(j)==list:
# 				for k in j:
# 					if type(k)==list:
# 						for l in k:
# 							if type(l)==list:
# 								for m in l:
# 									if type(m)==list:
# 										for n in m:
# 											if type(n)==list:
# 												for o in n:
# 													if type(o)==list:
# 														for p in o:
# 															if type(p)==list:
# 																for q in p:
# 																	if type(q)==list:
# 																		for r in q:
# 																			if type(r)==list:
# 																				for s in r:
# 																					if s>great:
# 																						great=s

# 																			else:
# 																				if r>great:
# 																					great=r

# 																	else:		
# 																		if q>great:
# 																			great=q
# 															else:
# 																if p>great:
# 																	great=p
# 													else:
# 														if o>great:
# 															great=o
# 											else:
# 												if n>great:
# 													great=n
# 									else:
# 										if m>great:
# 											great=m
# 							else:
# 								if l>great:
# 									great=l
# 					else:
# 						if k>great:
# 							great=k
# 			else:
# 				if j>great:
# 					great=j
# 	else:
# 		if i>great:
# 			great=i		 													 										

# print(great)
# print(index)


########################################################################################################

# Write a program that how many types to reached a no.

# number=int(input("Enter a no"))
# list1=[2,5,10]
# length=len(list1)
# empty=[]
# for i in range (0,len(list1)):
# 	k=list1[i]
# 	new=[]
# 	for j in range (0,number//list1[i]+1):
# 		if k*j==number:
# 			for c in range (j):
# 				new.append(k)			
# 	f=list1[length-3]+list1[length-2]
# 	for h in range(0,number//list1[i]+1):
# 		if f*h==number:
# 			for c in range(f):
# 				new.append(f)		
	
# 	empty.append(new)
# print(empty)


##############################################################################################

#Write a Python program to get the smallest number from a list. 

# list1=[2,5,9,8,1,7,89]
# length=len(list1)

# lower=list1[0]
# for i in list1:
# 	if i<lower:
# 		lower=i
# print(lower)


##################################################################################################

#Write a Python program to remove duplicates from a lis.

# list1=[2,2,5,9,8,7,12,89,78,89]
# new=[]
# for i in list1:
# 	if i not in new:
# 		new.append(i)
# print(new)


############################################################################################

# Write a Python program to check a list is empty or not. 

# list1=[1,2,5,8,7,9]
# if list1==[]:
# 	print('empty list')
# else:
# 	print("not empty list")

#######################################################################################

#Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# list1=[2,5,8,7,9,10,12,85,7,6]

# for i in list1:
# 	if i%2==0:
# 		list1.remove(i)
# print(list1)


#######################################################################################

# Write a program to find a sum of every list and print highest sum of list.\

# numbers = [
# [1,2,3,7,8,9,100000],
# [56,43,21,89,7600],
# [45,78,90,21,56,78],
# [24,56,89,90,10,11000000],
# [100, 123, 567]
# ]
# great=0
# new=[]
# for i in range (0,len(numbers)):
# 	sum=0
# 	count=0
# 	for j in numbers[i]:
# 		sum+=j
# 	new.append(sum)
# 	if sum>great:
# 		great=sum
# for k in range(len(new)):
# 	if great==new[k]:
# 		print(numbers[k],great)



###################################################################################

# write a program to find a character count how many times to came.

# list1=['highest', 'name', 'aman', 'dream', 'singing']
# new=[]
# rem=[]
# for i in list1:
# 	for j in i:
# 		rem.append(j)
# 		if j not in new:
# 			new.append(j)
# for i in new:
# 	c=0
# 	for j in rem:
# 		if i==j:
# 			c+=1

# 	print(i,'-',c,'times')


###############################################################################

#Write a program to find a employee data with his sir name.
# list1=['kumar Nayak','Aman kumar','Shabid khan','Atul pohwal']
# list2=[21,25,18,20]

# search_name=input("enter a name: ")
# for i in range (len(list1)):
# 	if search_name==list1[i]:
# 		print(list1[i],"age is",list2[i])
# 	elif search_name in list1[i]:
# 		print(list1[i])


# #############################################################################

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
y=[]
z=[]
while i<len(n):
	if n[i] not in y:
		y.append(n[i])
	else:
		z.append(n[i])
	i+=1
print(z) 