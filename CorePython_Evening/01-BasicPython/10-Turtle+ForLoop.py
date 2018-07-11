Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.shape('turtle')
>>> a = "Hello world"
>>> for i in a:
	print(i)

	
H
e
l
l
o
 
w
o
r
l
d
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> for i in range(1,11):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
>>> for i in range(11,21):
	print(i)

	
11
12
13
14
15
16
17
18
19
20
>>> for i in range(1,21,2):
	print(i)

	
1
3
5
7
9
11
13
15
17
19
>>> for i in range(2,22,2):
	print(i)

	
2
4
6
8
10
12
14
16
18
20
>>> a
'Hello world'
>>> a = [1,2,3,4,5,6,2,34,3,54,6,45,232]
>>> for i in a:
	print(i)

	
1
2
3
4
5
6
2
34
3
54
6
45
232
>>> x = 11
>>> for i in x:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for i in x:
TypeError: 'int' object is not iterable
>>> for i in range(11,111,11):
	for j in range(1,i/11):
		print(x,"x",j,"=",i)

		
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    for j in range(1,i/11):
TypeError: 'float' object cannot be interpreted as an integer
>>> for i in range(11,111,11):
	for j in range(1,i//11):
		print(x,"x",j,"=",i)

		
11 x 1 = 22
11 x 1 = 33
11 x 2 = 33
11 x 1 = 44
11 x 2 = 44
11 x 3 = 44
11 x 1 = 55
11 x 2 = 55
11 x 3 = 55
11 x 4 = 55
11 x 1 = 66
11 x 2 = 66
11 x 3 = 66
11 x 4 = 66
11 x 5 = 66
11 x 1 = 77
11 x 2 = 77
11 x 3 = 77
11 x 4 = 77
11 x 5 = 77
11 x 6 = 77
11 x 1 = 88
11 x 2 = 88
11 x 3 = 88
11 x 4 = 88
11 x 5 = 88
11 x 6 = 88
11 x 7 = 88
11 x 1 = 99
11 x 2 = 99
11 x 3 = 99
11 x 4 = 99
11 x 5 = 99
11 x 6 = 99
11 x 7 = 99
11 x 8 = 99
11 x 1 = 110
11 x 2 = 110
11 x 3 = 110
11 x 4 = 110
11 x 5 = 110
11 x 6 = 110
11 x 7 = 110
11 x 8 = 110
11 x 9 = 110
>>> for i in range(1,11):
	print(x,"x",i = i*x)

	
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    print(x,"x",i = i*x)
TypeError: 'i' is an invalid keyword argument for this function
>>> for i in range(1,11):
	print(x,"x",i ,'=', i*x)

	
11 x 1 = 11
11 x 2 = 22
11 x 3 = 33
11 x 4 = 44
11 x 5 = 55
11 x 6 = 66
11 x 7 = 77
11 x 8 = 88
11 x 9 = 99
11 x 10 = 110
>>> for i in range(4):
	turtle.forward(100)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.forward(5*i)
	turtle.left(45*i)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.forward(5*i)
	turtle.left(90)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(10*i)

	
Traceback (most recent call last):
  File "<pyshell#59>", line 2, in <module>
    turtle.circle(10*i)
  File "<string>", line 8, in circle
  File "C:\Python36\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36\lib\turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turtle.reset()
>>> for i in range(20):
	turtle.circle(10*i)
	turtle.left(10)

	
>>> turtle.reset()
>>> for i in range(20):
	turtle.circle(5*i)
	turtle.left(5*i)

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(50):
	turtle.circle(5*i)
	turtle.left(5*i)

	
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(50):
	turtle.circle(5*i)
	turtle.left(10)

	
>>> turtle.reset()
>>> turtle.color('red')
>>> turtle.speed(0)
>>> for i in range(50):
	turtle.circle(5*i)
	turtle.left(10)

	
>>> turtle.fillcolor('green')
>>> turtle.reset()
>>> turtle.color('red')
>>> turtle.fillcolor('green')
>>> turtle.speed(0)
>>> for i in range(50):
	turtle.circle(5*i)
	turtle.left(10)

	
>>> turtle.filling('yellow')
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    turtle.filling('yellow')
TypeError: filling() takes 0 positional arguments but 1 was given
>>> turtle.filling()
False
>>> 
