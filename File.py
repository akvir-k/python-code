
# counter=1
# exercise_txt=open('people1.txt')
# file_data=exercise_txt.read()
# for data in file_data:
# 	if '\n' in data:
# 		counter+=1

# print(counter)

# exercise_txt.close()




#######################################################################

# question2

# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# open_file=open('question3.txt','w')

# for bank_file in banks_list:
# 	open_file.write(bank_file +'\n')
# open_file.close()

# open_file=open('question3.txt')
# file_data=open_file.read()
# print(file_data)
# open_file.close()


##########################################################################

# open_file=open('people1.txt','r')
# w=open_file.read()
# open_file.close()

# w_split=w.split('\n')
# print(w_split)

# delhi_file=open('Delhi.txt','w')
# shimla_file=open('Shimla.txt','w')
# other_place=open('other_place.txt','w')
# delhi_file,shimla_file,other_place.close()
# for name in w_split:
# 	if 'delhi' in name:
# 		delhi_file=open('Delhi.txt','a')
# 		delhi_file.write(name+'\n')
# 		delhi_file.close()
# 	elif 'shimla' in name:
# 		shimla_file=open('Shimla.txt','a')
# 		shimla_file.write(name+'\n')
# 		shimla_file.close()
# 	else:
# 		other_place=open('other_place.txt','a')
# 		other_place.write(name+'\n')
# 		other_place.close()



import json
with open('user.json') as data_file:    
	data = json.load(data_file)
print data
users = data['users']

for user in data:
	print user
	counter = 0
	print "users full name is " + user['firstName'] + ' ' + user['lastName']
	while counter < len(user['details']):
		print "users mobile number is " + user['details'][counter]['mobileNo']
		print "users age  is " + user['details'][counter]['age']
		print "users city is " + user['details'][counter]['city']
