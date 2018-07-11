Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def show():
	print("This is return demo")
	return "Hello world"
	print("Will work after return statement")

	
>>> show()
This is return demo
'Hello world'
>>> def myLogic():
	x = 12
	return x*x

>>> myLogic()
144
>>> def printLogic():
	myLogic()

	
>>> printLogic()
>>> def printLogic():
	return myLogic()

>>> printLogic()
144
>>> import math
>>> def printLogic():
	val = myLogic()
	value = math.sqrt(val)
	return value

>>> printLogic()
12.0
>>> def myLogic(x):
	return x*x

>>> def printLogic(x):
	val = myLogic(x)
	print("Value after square is",val)
	value = math.sqrt(val)
	print("Value after square root is",value)
	return value

>>> printLogic(32)
Value after square is 1024
Value after square root is 32.0
32.0
>>> def calc(x,y):
	return x+y, x-y, x/y, x*y

>>> calc(12,11)
(23, 1, 1.0909090909090908, 132)
>>> add,sub,mul,div = calc(11,12)
>>> add
23
>>> sub
-1
>>> mul
0.9166666666666666
>>> div
132
>>> for a,b,c,d in calc(11,12):
	print(a,b,c,d)

	
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for a,b,c,d in calc(11,12):
TypeError: 'int' object is not iterable
>>> for a,b,c,d in calc():
	print(a,b,c,d)

	
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    for a,b,c,d in calc():
TypeError: calc() missing 2 required positional arguments: 'x' and 'y'
>>> 
