Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def func(x,y):
	return x + y

>>> func(1,2)
3
>>> lambda x,y : x + y
<function <lambda> at 0x0000022F86D13E18>
>>> 
>>> x = lambda x,y : x + y
>>> x(12,14)
26
>>> 
