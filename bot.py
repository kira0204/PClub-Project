from __future__ import print_function
try:
   	input = raw_input
except NameError:
   	pass

def max(a,b):
	if(a>b):
		max = a
	else
		max = b

def friends():
	response = input('How are your friends meeting up with your expectations?\n')
	if(response == positive)
		response = input('Have you broken up with someone recently?'\n)
		if(response == positive)
			print('A3')
			print('finisher')
		else:
			print('A2')
			print('finisher')
	else:
		print('A1')
		print('finisher')

def sad4():
	response_friends = input('How are things going on with your friends?\n')
	response_family  = input('How is your relationship with your parents?\n')
	response_worklife = input('How is your work or academic life going on?\n')
	if(response_friends > max(response_family,response_work)
		friends()
	else:
		if(response_family > response_work)
			family()
		else:
			work()
def sad2():
	response = input('Please share your feelings?\n')
	if(response == positive)
		response = input('Among the thoughts occuring in your mind which one upsets you the most?\n')
		response = input('Why do you think it upsets you?\n')
		# response = input('COPY FROM counselling connection.com)
		response = input('Are there signs that contrary could be true?\n')
		if(response == positive)
			print("I'm gld that you realised that the opposite could be true.Best of luck for your future endeavours.Bye!")
		else:
			sad4()
def sad():
	response = input('Mild sympathy.Is this serious?\n')
	if(response == positive):
		response = input('Do you really need help?\n')
		if(response == positive)
			print('bye!bye')
		else:
			sad3()
	else:
		sad2()

def sad3():
	response = input('Feel comfortable.Could you breifly explain about your day?\n')
	response = input('What are the activities that make up your most of the day?\n')
	response = input('It seems you are comfortable talking about yourself.Could you share your feelings?\n')
		if(response == positive)
			sad2()
		else:
			sad4()
	
print('introduction')
name = input('What's your name?')
print('how are you feeling?')
response = input()
if (response == positive):
	print('That's good! Are you really this happy?')
	response = input()
	if (response == positive):
		print('You seem to be really happy.Wanna sign off?')
		response = input()
			if(response == positive):
				print('bye bye!')
			else:
				print('Is this really something bothering you?')
				response = input()
				if(response == positive):
					print('bye!bye')
				else:
					sad()
	else:
		sad()
else:
	sad3()																									
