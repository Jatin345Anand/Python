Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = ['Ram', 98989898, 88.67, True]
>>> print(a)
['Ram', 98989898, 88.67, True]
>>> a[0]
'Ram'
>>> a[1]
98989898
>>> a[2]
88.67
>>> a[3]
True
>>> for i in range(len(a)):
	print(i)

	
0
1
2
3
>>> for i in range(len(a)):
	print(a[i])

	
Ram
98989898
88.67
True
>>> for i in a:
	print(i)
	print(type(i))

	
Ram
<class 'str'>
98989898
<class 'int'>
88.67
<class 'float'>
True
<class 'bool'>
>>> for i in a:
	print(i)
	if i == True:
		print("Congrats,You are eligible")
	else:
		print("Try Next Time...")

		
Ram
Try Next Time...
98989898
Try Next Time...
88.67
Try Next Time...
True
Congrats,You are eligible
>>> for i in a:
	print(i)
	if type(i) == 'bool':
		print("Congrats,You are eligible")
	else:
		print("Try Next Time...")

		
Ram
Try Next Time...
98989898
Try Next Time...
88.67
Try Next Time...
True
Try Next Time...
>>> for i in a:
	print(i)
	if type(i) == 'bool':
		print("Congrats,You are eligible")

		
Ram
98989898
88.67
True
>>> for i in a:
	print(i)
	if type(i) == "<class 'bool'>":
		print("Congrats,You are eligible")

		
Ram
98989898
88.67
True
>>> for i in a:
	print(i)
	if type(i) == <class 'bool'>:
		print("Congrats,You are eligible")
		
SyntaxError: invalid syntax
>>> users = {'user_name':'Ram', 'user_num':989898989, 'user_per':88.88, 'user_eligible':True}
>>> users
{'user_name': 'Ram', 'user_num': 989898989, 'user_per': 88.88, 'user_eligible': True}
>>> users['user_name']
'Ram'
>>> users['user_num']
989898989
>>> users.keys()
dict_keys(['user_name', 'user_num', 'user_per', 'user_eligible'])
>>> users.values()
dict_values(['Ram', 989898989, 88.88, True])
>>> for i in users:
	print(i)

	
user_name
user_num
user_per
user_eligible
>>> users.items()
dict_items([('user_name', 'Ram'), ('user_num', 989898989), ('user_per', 88.88), ('user_eligible', True)])
>>> for i in users.items():
	print(i)

	
('user_name', 'Ram')
('user_num', 989898989)
('user_per', 88.88)
('user_eligible', True)
>>> for i in users.items():
	print(i)
	if users['eligible'] == True:
		print("Congrats, You are eligible")

		
('user_name', 'Ram')
Traceback (most recent call last):
  File "<pyshell#45>", line 3, in <module>
    if users['eligible'] == True:
KeyError: 'eligible'
>>> for i in users.items():
	print(i)
	if users['user_eligible'] == True:
		print("Congrats, You are eligible")

		
('user_name', 'Ram')
Congrats, You are eligible
('user_num', 989898989)
Congrats, You are eligible
('user_per', 88.88)
Congrats, You are eligible
('user_eligible', True)
Congrats, You are eligible
>>> for i in users.items():
	print(i)
	print(i['eligible'])

	
('user_name', 'Ram')
Traceback (most recent call last):
  File "<pyshell#49>", line 3, in <module>
    print(i['eligible'])
TypeError: tuple indices must be integers or slices, not str
>>> for i in users.items():
	print(i)
	print(i['user_eligible'])

	
('user_name', 'Ram')
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    print(i['user_eligible'])
TypeError: tuple indices must be integers or slices, not str
>>> for i in users.items():
	print(i)
	print(i[-1])

	
('user_name', 'Ram')
Ram
('user_num', 989898989)
989898989
('user_per', 88.88)
88.88
('user_eligible', True)
True
>>> for i in users.items():
	print(i)
	if users[-1] == True:
		print("Congrats, You are eligible")

		
('user_name', 'Ram')
Traceback (most recent call last):
  File "<pyshell#55>", line 3, in <module>
    if users[-1] == True:
KeyError: -1
>>> for i in users.items():
	print(i)
	if i[-1] == True:
		print("Congrats, You are eligible")

		
('user_name', 'Ram')
('user_num', 989898989)
('user_per', 88.88)
('user_eligible', True)
Congrats, You are eligible
>>> for i in users.values():
	print(i)
	if i[-1] == True:
		print("Congrats, You are eligible")

		
Ram
989898989
Traceback (most recent call last):
  File "<pyshell#59>", line 3, in <module>
    if i[-1] == True:
TypeError: 'int' object is not subscriptable
>>> for i in users.values():
	print(i)
	if i == True:
		print("Congrats, You are eligible")

		
Ram
989898989
88.88
True
Congrats, You are eligible
>>> a
['Ram', 98989898, 88.67, True]
>>> for i in a:
	print(i)
	if i == True:
		print("Congrats, You are eligible")

		
Ram
98989898
88.67
True
Congrats, You are eligible
>>> userData = [{'user_name':'Ram', 'user_num':989898989, 'user_per':88.88, 'user_eligible':True},{'user_name':'Shyam', 'user_num':787878989, 'user_per':68.88, 'user_eligible':False},{'user_name':'Rohan', 'user_num':878798878, 'user_per':81.18, 'user_eligible':True},{'user_name':'Gopal', 'user_num':9899879879, 'user_per':78.80, 'user_eligible':True},{'user_name':'Akash', 'user_num':989897789, 'user_per':70.88, 'user_eligible':False}]
>>> userData[0]
{'user_name': 'Ram', 'user_num': 989898989, 'user_per': 88.88, 'user_eligible': True}
>>> userData[1]
{'user_name': 'Shyam', 'user_num': 787878989, 'user_per': 68.88, 'user_eligible': False}
>>> userData[2]
{'user_name': 'Rohan', 'user_num': 878798878, 'user_per': 81.18, 'user_eligible': True}
>>> for i in userData:
	print(i)

	
{'user_name': 'Ram', 'user_num': 989898989, 'user_per': 88.88, 'user_eligible': True}
{'user_name': 'Shyam', 'user_num': 787878989, 'user_per': 68.88, 'user_eligible': False}
{'user_name': 'Rohan', 'user_num': 878798878, 'user_per': 81.18, 'user_eligible': True}
{'user_name': 'Gopal', 'user_num': 9899879879, 'user_per': 78.8, 'user_eligible': True}
{'user_name': 'Akash', 'user_num': 989897789, 'user_per': 70.88, 'user_eligible': False}
>>> for i in userData:
	print(i)
	if i['user_eligible'] == True:
		print("Congrats {}, You are eligible".format(i['user_name']))

		
{'user_name': 'Ram', 'user_num': 989898989, 'user_per': 88.88, 'user_eligible': True}
Congrats Ram, You are eligible
{'user_name': 'Shyam', 'user_num': 787878989, 'user_per': 68.88, 'user_eligible': False}
{'user_name': 'Rohan', 'user_num': 878798878, 'user_per': 81.18, 'user_eligible': True}
Congrats Rohan, You are eligible
{'user_name': 'Gopal', 'user_num': 9899879879, 'user_per': 78.8, 'user_eligible': True}
Congrats Gopal, You are eligible
{'user_name': 'Akash', 'user_num': 989897789, 'user_per': 70.88, 'user_eligible': False}
>>> for i in userData:
	print(i)
	if i['user_eligible'] == True:
		print("Congrats {}, You are eligible".format(i['user_name']))
	else:
		print("Sorry {},You are not eligible".format(i['user_name']))

		
{'user_name': 'Ram', 'user_num': 989898989, 'user_per': 88.88, 'user_eligible': True}
Congrats Ram, You are eligible
{'user_name': 'Shyam', 'user_num': 787878989, 'user_per': 68.88, 'user_eligible': False}
Sorry Shyam,You are not eligible
{'user_name': 'Rohan', 'user_num': 878798878, 'user_per': 81.18, 'user_eligible': True}
Congrats Rohan, You are eligible
{'user_name': 'Gopal', 'user_num': 9899879879, 'user_per': 78.8, 'user_eligible': True}
Congrats Gopal, You are eligible
{'user_name': 'Akash', 'user_num': 989897789, 'user_per': 70.88, 'user_eligible': False}
Sorry Akash,You are not eligible
>>> D1 = {'a' : 'one', 'b' : 'two', 'c' : 'three', 'd' : 'four'}
D2 = {'c' : 'five', 'd' : 'six', 'e' : 'seven', 'f' : 'eight'}
SyntaxError: multiple statements found while compiling a single statement
>>> D1 = {'a' : 'one', 'b' : 'two', 'c' : 'three', 'd' : 'four'}
>>> D2 = {'c' : 'five', 'd' : 'six', 'e' : 'seven', 'f' : 'eight'}
>>> D = {}
>>> for d in D1:
	D[d] = D1[d]
	print(D)

	
{'a': 'one'}
{'a': 'one', 'b': 'two'}
{'a': 'one', 'b': 'two', 'c': 'three'}
{'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four'}
>>> D
{'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four'}
>>> for d in D2:
	D[d] = D2[d]
	print(D)

	
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'four'}
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'six'}
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'six', 'e': 'seven'}
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'six', 'e': 'seven', 'f': 'eight'}
>>> a
['Ram', 98989898, 88.67, True]
>>> D
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'six', 'e': 'seven', 'f': 'eight'}
>>> D
{'a': 'one', 'b': 'two', 'c': 'five', 'd': 'six', 'e': 'seven', 'f': 'eight'}
>>> for d in D:
	print(d, D[d])

	
a one
b two
c five
d six
e seven
f eight
>>> 
