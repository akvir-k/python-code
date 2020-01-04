
# Write a program to find which no is divisible by all range of no.

# input_user=int(input('Enter a no: '))
# continue_no=1
# while True:
# 	ran_user=1
# 	while ran_user<=input_user:
# 		if continue_no%ran_user==0:
# 			ran_user+=1
# 			continue
# 		else:
# 			break
# 	else:
# 		break
# 	print(continue_no)
# 	continue_no+=1
# print(continue_no)


#####################################################################

# a=[1,2,[3,4],3,5,[12,3,4,5,[2,34,[4,5,[5333,3,3,[333,3,3,3,]],[242,4,4,4,[44,4,44,[75,3,-3,4,0,[786,[1]]]]]]]]]


# def sum_of_list(user_input,list1):
# 	new=[]
# 	sum1=0
# 	for i in list1:

# 		if user_input==1:
# 			if type(i)!=int:
# 				sum1=sum1+sum_of_list(user_input,i)
# 			else:
# 				sum1+=i

# 		elif user_input==2:
# 			if type(i)!=int:
# 				new=new+sum_of_list(user_input,i)
# 			else:
# 				new.append(i)
# 	if user_input==1:
# 		return sum1
# 	else:
# 		return new

# def Highest_lowest_No(user_input,no):
# 	vairab=0

# 	arreng_list=sum_of_list(2,no)
# 	lowest=arreng_list[0]
# 	for i in arreng_list:
# 		if user_input==3:
# 			if i>vairab:
# 				vairab=i
# 		elif user_input==4:
# 			if i<lowest:
# 				lowest=i
# 	if user_input==3:
# 		return vairab
# 	else:
# 		return lowest


# input_user=int(input('Enter a user (1).sum of all list (2). Find the greater no (3). find lowest no (4) Make a sepreate list '))

# if input_user==1 or input_user==2:
# 	print(sum_of_list(input_user,a))
# elif input_user==3 or input_user==4:
# 	print(Highest_lowest_No(input_user,a))
# else:
# 	print('wrong input')
###############################################################################

# perfect no with function.

# number=int(input('Enter a number: '))

# def perfect_no(x):
# 	sum1=0
# 	for no in range(1,x//2+1):
# 		if x%no==0:
# 			sum1+=no
# 	if sum1==x:
# 		print(x,'perfect no')
# for user_no in range(1,number+1):
# 	perfect_no(user_no)



##########################################################################

# Write a program to make stone paper sezire game:
# from random import randint


# def computer_choose():
# 	move=['Rock','Paper','Scissor']
# 	random_move=randint(0,2)
# 	computer_playing=move[random_move]
# 	return computer_playing

# def game_rule(x):
# 	computer_choice=computer_choose()
# 	if x=='Rock':
# 		if computer_choice=='Rock':
# 			print('Tied match')
# 		elif computer_choice=='Paper':
# 			print('You loss the match Because computer choose paper')
# 		else:
# 			print('you won the match Because computer choose scissor')
# 	elif x=='Paper':
# 		if computer_choice=='Paper':
# 			print('Match Tied')
# 		elif computer_choice=='Scissor':
# 			print('you loss the match Because computer choose scissor')
# 		else:
# 			print('you won the match because computer choose rock')
# 	elif x=='Scissor':
# 		if computer_choice=='Scissor':
# 			print('Match Tied')
# 		elif computer_choice=='Paper':
# 			print('you won the match because computer choose paper')
# 		else:
# 			print('you loss the match because computer choose rock')
# 	else:
# 		print ('wrong input')

# while True:
# 	user_input=input('Enter a user. Rock/Paper/Scissor')
# 	game_rule(user_input)
# 	again_play=int(input(' Do you want to play again:-)1.yes/2.No'))
# 	if again_play==1:
# 		continue
# 	else:
# 		break


 ##################################################################################

 

####################################################################

# number=int(input('enter a no'))

# i=2
# new=[]
# while i<=number//2+1:
# 	if number%i==0:
# 		new.append(i)
# 	print(i)	
# 	i+=1

# print(new)
# for i in new:
# 	j=2
# 	while j<=i//2+1:
# 		if i%j==0:
# 			break
# 		else:
# 			j+=1n
# 	else:
# 		print(i)

y=[]
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
duplicate=0
number=0
length=len(n)
while i<length:
	number=n[i]
	if number not in y:
		j=i+1
		while j<length:
			if number==n[j]:
				duplicate=n[j]
				y.append(duplicate)
				break
			j+=1				
	i+=1
print(y)			

