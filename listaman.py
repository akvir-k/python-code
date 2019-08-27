# names_list=["aman","shyam",'simran']
# int_list=[23,25,26,28,29]
# float_list=[23.1,25.8,25.4,29.6]
# print(names_list)
# print(int_list)
# print(float_list)
# print (type(names_list))
# print (type(int_list))
# print(type(float_list))
# print (int_list[0])
# names_list.append ("shivam")
# print (names_list)
# names_list.pop(2)
# print(names_list)




# students__marks=[23,25,26,29,12,36,89,24,16]
# list_length=len(students__marks)
# index=0
# less=0
# more=0
# while(index<list_length):
# 	marks=students__marks[index]
# 	if marks<50:
# 		less=less+1
# 		print(marks)
# 	else:

# 		more=more+1

# 	index=index+1
# print("marks more then50 ",more)
# print("marks less then 50 ",less)





###############################################################
# # define how len function work
# def length(x):
# 	count = 0
# 	for i in x:
# 		count+=1
# 	return count



# a = [1,2,3,5,6,7]

# print(length(a))



###############################################################
# get the length without using len funtion.
# number=[1,2,3,4,5,6,7,8]
# i=0
# num=0
# while True:
# 	if number==[]:
# 		print(num)
# 		break
# 	else:
# 		number.remove(number[i])
# 		num+=1

##########################################################
# #

# numbers=[50, 29, 23, 70, 56, 35, 5, 10, 7]
# no=len(numbers)
# i=0
# while i<no:         
# 	value=numbers[i]
# 	if(20<value<40):
# 		print(i)
# 		print(value)
# 		i=i+1	
# 	else:
# 		i=i+1
###################################################################
# reverse the list without using reverse funtion


# places=["delhi","gujrat","rajasthhan","mumbai"]
# list1=[]
# no=len(places)
# i=-1
# while i<no:
# 	if places==[]:
# 		break
# 	else:
# 		list1.append(places[i])
# 		places.remove(places[i])
# 	no=no+1
# print(list1)

################################################################################
# print greatest no in list without using a any list function like append and remove

# numbers=[50, 89, 23, 70, 56, 35, 5, 10, 97]
# i=0
# b=1
# while i<len(numbers):
#     while b<len(numbers):
#         if numbers[i]<numbers[b]:
#             greater=numbers[b]
#             break            
#         else:
#             b+=1
        
#     i=i+1
# print(greater)

numbers=[50, 89, 23, 70, 56, 35, 5, 10, 97]
no=[]
i=0
b=0
while i<len(no):
	no.append(numbers[i])
	numbers.remove(numbers[i])
	if no<numbers:
		break
	else:
		i+=1
print(no)



