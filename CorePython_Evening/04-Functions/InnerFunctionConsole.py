Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def outer(x):
	print("This is outer function...")
	def inner()
	
SyntaxError: invalid syntax
>>> def outer(x):
	print("This is outer function...")
	def inner():
		print("This is inner function...")
		return x
	return inner

>>> print(outer)
<function outer at 0x0000024C0AEB76A8>
>>> outer(2)
This is outer function...
<function outer.<locals>.inner at 0x0000024C0A3C3E18>
>>> outer(2)()
This is outer function...
This is inner function...
2
>>> a = outer(2)
This is outer function...
>>> a
<function outer.<locals>.inner at 0x0000024C0A3C3E18>
>>> a()
This is inner function...
2
>>> def outer(x):
	print("This is outer function...")
	def inner():
		print("This is inner function...")
		x += 1
		return x
	return inner

>>> outer(2)()
This is outer function...
This is inner function...
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    outer(2)()
  File "<pyshell#14>", line 5, in inner
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def outer(x):
	print("This is outer function...")
	def inner():
		print("This is inner function...")
		y = x
		y += 1
		return y
	return inner

\
>>> outer(2)()
This is outer function...
This is inner function...
3
>>> outer(2)()
This is outer function...
This is inner function...
3
>>> outer(2)()
This is outer function...
This is inner function...
3
>>> a = outer(2)
This is outer function...
>>> a()
This is inner function...
3
>>> a()
This is inner function...
3
>>> a()
This is inner function...
3
>>> def outer(x):
	print("This is outer function...")
	def inner():
		print("This is inner function...")
		def innermost():
			print("This is inner most function...")
			return x
		return innermost
	return inner

>>> outer(2)()()
This is outer function...
This is inner function...
This is inner most function...
2
>>> 
