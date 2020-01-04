
# def ask_question():
# 	for i in range(100):
# 		print('Who is the Founder of Facebook\n')
# 		print(' - Zuckeburg\n','- Bill Gates\n','- Steves job\n','- Larry Page')
# ask_question()indi

######################################################################

# def language(name,lang):
# 	if lang=='Hindi':
# 		print('Namaste',name)
# 		print('How are you')
# 	elif lang=='Punjabi' or lang=='punjabi':
# 		print('Toda ki hall hai',name)
# 		print('kasi kat rahi hai')
# 	elif lang=='Tamil':
# 		print('Vanakam',name)
# 		print('epdi irukinga')
# 	else:
# 		print('Chal nikal yaha se')
# 		print('dubara try kar')
# language('Aman','punjabi')
# language('Sam','Tamil')
# language('Dream','sanskrit')
# language('Seem','Hindi')


#######################################################################

# def number():
# 	list1=[2,4,9,12],[4,5,9,12]
# 	i=list1[0]
# 	for x in range(len(i)):
# 		if list1[0][x]%2==0 and list1[1][x]%2==0:
# 			print('yes')
# 		else:
# 			print('no')
# number()

###################################################################

# def add(x,y):
# 	b=x+y
# 	return b
# a=add(2,3)
# print(a)

#####################################################

# Write a program to make a calculater with function.

# def calc(x,y,operation):
# 	if operation=='add':
# 		return x+y
# 	elif operation=='substract':
# 		return x-y
# 	elif operation=='multiply':
# 		return x*y
# 	elif operation=='power':
# 		return x**y
# 	elif operation=='divide':
# 		if y==0:
# 			print('Not possible')

# 		else:
# 			return x/y
# 	else:
# 		return print('wrong input')
# no1=int(input('Enter a no'))
# no2=int(input('Enter a second no'))
# op=input('Enter a operation')
# a=calc(no1,no2,op)
# print(a)


################################################################################

# Write a program to print 1 to 1000 with some contion.
'''Agar number 3 se divisible hai toh "nav" print karvao.
Agar number 7 se divisible hai toh "gurukul" print karvao.
Agar number 21 se divisible hai toh "navgurukul" print karvao.'''

# def divisible(no):
# 	if no%3==0 and no%7==0:
# 		return ('Navgurukul')
# 	elif no%7==0:
# 		return ('Gurukul')
# 	elif no%3==0:
# 		return ('Nav')
# 	else:
# 		return no
# for i in range(100):
# 	a=divisible(i)
# 	print(a)

#############################################################################

'''Iss program mein hum students ki ginti aur ek student ke kharche se hisaab se pure NavGurukul ka ek mahine ka kharcha nikalenge

raw_input ka use kar ke do values ka input lo:

Number of students
Ek student ka kharcha'''

# def budget(a):
# 	if a<50000:
# 		return ('budget ke andar hai')
# 	else:
# 		return ('budget ke bahar hai')
# number_of_student=int(input('Enter a no'))
# bud=int(input('Enter a per student value'))
# b=budget(number_of_student*bud)
# print(b)


# ########################################################################

# def calc(x,y,operation):
# 	if operation=='add':
# 		return x+y
# 	elif operation=='substract':
# 		return x-y
# 	elif operation=='multiply':
# 		return x*y
# 	elif operation=='power':
# 		return x**y
# 	elif operation=='divide':
# 		if y==0:
# 			print('Not possible')

# 		else:
# 			return x/y
# 	else:
# 		return print('wrong input')
# list1=[]
# no=([2,5,9,10],[1,2,8,9])
# new=no[0]
# for i in range(len(new)):
# 	b=calc(no[0][i],no[1][i],'multiply')
# 	list1.append(b)
# print(list1)



###############################################################

# def password(word):
# 	if 6>len(word)<16:
# 		if word in string.digits:
# 			return 'Strong Password'
# 		else:
# 			return 'weak password'
# 	else:
# 		return 'weak password'
# word=input('enter a password')
# new=[]
# import string
# for i in word:
# 	if i in string.ascii_lowercase or i in string.ascii_uppercase:
# 		new.append(i)

# 	elif i in string.punctuation:
# 		new.append(i)
# 	else:
# 		b=int(i)
# 		new.append(b)
# print(new)



###########################################################################

'''raw_input ka use kar ke
 3 alag variables mein 3 integers ka input lein. 
 Input lene ke baad inn 3 mein se sabse bade number ko print karo'''


# def find(x,y,z):
# 	if y<x>z:
# 		return(x,'is highest digits')
# 	elif x<y>z:
# 		return(y,' is highest digits')
# 	else:
# 		return(z,'is highest digits')

# no1=int(input())
# no2=int(input())
# no3=int(input())

# great=find(no1,no2,no3)
# print(great)


########################################################################

# Write a program to calculate factiorial no data.

# def fact(no):
# 	sum1=1
# 	for i in range (no,1,-1):
# 		sum1=sum1*i
# 	return(sum1)

# no=int(input())
# factorial_calc=fact(no)
# print(factorial_calc)

###################################################################


# list1 = [1, 342, 75, 23, 98]
# list2 = [75, 23, 98, 12, 78, 10, 1]
# new=[]
# def match(x):
# 	if i in list2:
# 		return new.append(i)

# for i in list1:
# 	d=match(i)
# print(new)


##################################################################

# list1 = [1, 5, 10, 12, 16, 20]
# list2 = [1, 2, 10, 13, 16]
# new=list1
# def combined(x):
# 	if x not in new:
# 		return new.append(x)
# for i in list2:
# 	d=combined(i)
# print(new)

##################################################################
# def is_leap(year):
#     if year%4==0 and (year%400==0 or year%100!=0):

#         return True
#     else:
#         return False
    
#     # Write your logic here
    

# year = int(input())
# print(is_leap(year))
	

###############################################################

# Write a program to no is harshed no and not?


# def Harshed(x):
# 		changed_string=str(i)
# 		sum_in_no=0
# 		for add in changed_string:
# 			sum_in_no=sum_in_no+int(add)

# 		if i%sum_in_no==0:
# 			print(i,'Harshed no') 
# 		# 	return 'Not a Harshed no'
# Input_number=int(input("Enter a no"))

# for i in range(1,Input_number+1):
# 	output=Harshed(i)
# 	# print(i,output)


#############################################################################

# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]


# for counter in range(len(big_list)):
# 	for inside_counter in big_list[counter]:
# 		print(inside_counter)
# 	print('----------------')


#######################################################################

'''ocho aapke paas ek school ki class mein har student ke har subject ke marks hain. Jaise
# '''
# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]

# def greater_Marks(x):
# 	great=0
# 	for inside_loop in marks[x]:
# 		if inside_loop>great:
# 			great=inside_loop
# 	return great

# for outside_loop in range(len(marks)):
# 	output=greater_Marks(outside_loop)
# 	print(output)

#############################################################################

# sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# sentense1=[]
# def break_into_words():
# 	word_add=''
# 	for i in sentence:
# 		if i==' ':
# 			sentense1.append(word_add)
# 			word_add=''
# 		else:
# 			word_add+=i
# break_into_words()
# print(sentense1)


#################################################################################

# def numbers_less_than_twenty(list):
# 	counter = 0
# 	new1=[]
# 	while counter < len(list):
# 		item = list[counter]
# 		if item < 20:
# 			new1.append(item)
# 			counter+=1
# 		else:
# 			counter+=1
# 	return new1

	
# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# num_list_sub_20=numbers_less_than_twenty(num_list)

# print "Initial list", num_list
# print "List that doesn't contain numbers greate than 20", num_list_sub_20

#####################################################################################

# def word_divide(x):
# 	add=[]
# 	word_list=""
# 	for word in x:
# 		if word==' ':
# 			add.append(word_list)
# 			word_list=''
# 		else:
# 			word_list+=word
# 	else:
# 		add.append(word_list)
# 	return add
# user_enter=input('Enter a text')
# user_word_output=word_divide(user_enter)
# print(user_word_output)


############################################################################################

# write a program encrypted message and decrepted message

# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# def Encryped(plain_message):
# 	choice=1
# 	for word in plain_message:
# 		if word in chars:
# 			index_chars=find_index(word,choice)
# 			encry_value=shifted_chars[index_chars]
# 	return encry_value

# def Decrypted(Encry_text):
# 	choice=2
# 	for word in Encry_text:
# 		index_chars=find_index(word,choice)
# 		decry_value=chars[index_chars]
# 	return decry_value

# def find_index(query,choice):
# 	index=0
# 	counter=0
# 	if choice==1:
# 		for chars_list in chars:
# 			if query == chars_list:
# 				index=counter
# 			else:
# 				counter+=1
# 	elif choice==2:
# 		for chars_list in shifted_chars:
# 			if query==chars_list:
# 				index=counter
# 			else:
# 				counter+=1
# 	return index


# encryped_msg=''

# Choice_user=int(input('What do you want to do: 1.Encryption 2.Decryption: '))
# user_input=input('Enter a message: ')

# for message in user_input:
# 	if Choice_user==1:
# 		plain_message=Encryped(message)
# 		encryped_msg+=plain_message
# 	elif Choice_user==2:
# 		encrypted_message=Decrypted(message)
# 		encryped_msg+=encrypted_message
# print(encryped_msg)


#####################################################################################

# Write a program of Alien Fighter game:

# from random import randint
# def report(Health_Alian):

# 	if Health_Alian==10:
# 		return ' you Defeat by Alian'
# 	elif 5<Health_Alian<10:
# 		return 'you are try great but no affected alian ship, you need more powerful weapon'
# 	elif 0<Health_Alian<=5:
# 		return 'Most of the part damage of Alian ship try more attack to vanqulised to alian'

# 	else:
# 		return 'You defeat to Alian'

# def Fight(Attack):

# 	if Attack==1 or Attack==2:
# 		print('You were attacking from nuclear weapon')
# 		damage=randint(0,10)
# 	elif Attack==3:
# 		print('You were attacking from missiles')
# 		damage=randint(0,5)
# 	else:
# 		print(' You were running because you do not have any weapon')
# 		damage=0
# 	print(damage)
# 	return damage

# Alian= True
# Health_Alian=10
# while Alian==True:

# 	user_input=int(input('What do you want to do:1.Attack,2.Hit,3.Fight,4.Run:' ))
# 	fight_report=Fight(user_input)
# 	Health_Alian-=fight_report
# 	Alian_report=report(Health_Alian)
# 	print(Alian_report)
# 	if Health_Alian<0:
# 		Alian=False
# 	elif Health_Alian==10:
# 		Alian=False



#############################################################################
'''Kisi bhi element ko nikalne ke liye, aapko peechle element mei 3 add karna hai.
Base Case ka dhyaan rakhein'''

'''1, 4, 7, 10, 13, 16 …'''

# def pattern(x):
# 	if x==1:
# 		return 1
# 	else:
# 		return pattern(x-1)+3

# user_input=int(input("Enter the user input: "))

# for i in range(1,user_input+1):
# 	print(pattern(i))



###############################################################################

# def even_odd_patterrn(x):
# 	if x==1:
# 		return 10
# 	elif x%2==0:
# 		return even_odd_patterrn(x-1)+1
# 	else:
# 		return even_odd_patterrn(x-1)*10

# number=int(input())
# for i in range(1,number+1):
# 	print(even_odd_patterrn(i))


#####################################################################
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
# number=int(input('enter a no'))

# i=2
# new=[]
# while i<=number:
# 	if number%i==0:
# 		new.append(i)
# 		print(new)
# 	i+=1
# print(new)
# for i in new:
# 	j=2
# 	while j<=i//2+1:
# 		if i%j==0:
# 			break
# 		else:
# 			j+=1
# 	else:
# 		print(i)


###############################################################################
# import random

# rules = [ "[INTEGER]", "[NESTED_LIST, INTEGER]", "[INTEGER, NESTED_LIST]", "NESTED_LIST + NESTED_LIST"]

# def generateRandomNumber():
#     return random.randrange(1, 20)

# def generateRandomNestedList(x):
#     random_rule = random.randrange(4)
#     if random_rule == 0:
#         return [generateRandomNumber()]

#     elif random_rule == 1:
#         return [generateRandomNestedList(), generateRandomNumber()]

#     elif random_rule == 2:
#         return [generateRandomNumber(), generateRandomNestedList()]

#     elif random_rule == 3:
#         return generateRandomNestedList() + generateRandomNestedList()

# a=[1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]
# print (generateRandomNestedList(a))



#############################################################################

# i=2
# while True:
# 	j=1
# 	while j<=10:
# 		if i%j==0:
# 			j+=1
# 			continue
# 		else:
# 			break
# 	else:
# 		print(i)
# 		break
# 	i+=1



# def happy_range(x):
# 	squ=0
# 	assign=x
# 	new=[]
# 	while True:
# 		if x==1:
# 			print(x)
# 			break
# 		else:
# 			sum1=0
# 			for i in str(x):					# loop commaned
# 				squ=int(i)*int(i)				# giving to square value
# 				sum1=sum1+squ 	 				# assign value in sum1
# 		if sum1==1:
# 			print(assign)
# 			break
# 		elif sum1 in new:		
# 			break
# 		else:
# 			new.append(sum1)
# 			x=sum1
# user_input=int(input('enter a range give by user'))

# for i in range(1,user_input+1):
# 	happy_range(i)


#####################################################################################

# write a program to encrypted message and decrypted message with ord and chr funtion.

# def Encrypted_msg():
# 	message=input('Enter a message for Encryption: ')
# 	convert_in_no=[ord(value)+3 for value in message ]
# 	Encrypt_message= [chr(encrypted) for encrypted in convert_in_no]
# 	print(''.join(Encrypt_message))

# def Decrypted_msg():
# 	message=input('Enter a message for Decryption: ')
# 	convert_in_no=[ord(value)-3 for value in message ]
# 	Decrypted_message=[chr(value) for value in convert_in_no ]
# 	print(''.join(Decrypted_message))

# while True:
# 	choice=input('What do you want to do: (E) Encrypt to message (D) Decrypt to message:')
# 	if choice=='E' or choice=='e':
# 		Encrypted_msg()
# 	elif choice=='D' or choice=='d':
# 		Decrypted_msg()
# 	else:
# 		print('wrong input value')

# 	again_play=input('Do you want to play again: Y:yes and N:No:  ')

# 	if again_play=='yes' or again_play=='y' or again_play=='Y':
# 		continue
# 	else:
# 		break


#############################################################################################
import random

def secrate(numdigits):
	no=list(range(10))
	random.shuffle(no)
	sec_no=''
	for i in range(len(numdigits)):
		sec_no+=str(no[i])
	return sec_no

def clues(user_input,secrate_num):

	getcluse=[]
	if user_input==secrate_num:
		return 'you got it a secrete no '
	else:
		for i in range(len(user_input)):
			if user_input[i]==secrate_num[i]:
				getcluse.append('fermi')
			
			elif user_input[i] in secrate_num:
				getcluse.append('Pico')

			else:
				getcluse.append('None')
	return getcluse
def report(guessNum):

	for i in range(len(guessNum)):
		if 'Pico' in guessNum[i]:
			print('Guess No is right but postion is wrong')
		elif 'None' in guessNum[i]:
			print('No is not match and wrong guess')
		else: 
			print('Guess No is right and postion is also right')

def guess_time(list):
	if 'Pico' in list:
		return False
	elif 'None' in list:
		return False
	else:
		return True

# main function
flag=False
numGuess=0
while True:
	while numGuess<10: 
		user_input=input('Enter a number given by user: ')

		secrate_num=secrate(user_input)

		guessvalue=clues(user_input,secrate_num)
		print(guessvalue)
		report(guessvalue)
		print(secrate_num)

		flag=guess_time(guessvalue)
		if flag is True:
			break
		else:
			print('Guess no again')
		numGuess+=1
			
	else:
		print('You are using maximum time but you can not find the no')
	user_input=int(input(' Do you want to play again: 1.Yes 2.no'))
	if user_input==1:
		continue
	else:
		break


######################################################################################



