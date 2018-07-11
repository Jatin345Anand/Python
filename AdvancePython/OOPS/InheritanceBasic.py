Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Parent():
	def display():
		print("This display belongs to parent")

	
>>> class Parent():
	def display(self):
		print("This display belongs to parent")

		
>>> class Child(Parent):
	def displayChild(self):
		print("This display belongs to child")

		
>>> obj = Child()
>>> obj.displayChild()
This display belongs to child
>>> obj.display()
This display belongs to parent
>>> class Child(Parent):
	def displayChild(self):
		print("This display belongs to child")
	def display(self):
		print("This display also belongs to child")

		
>>> obj = Child()
>>> obj.display()
This display also belongs to child
>>> class Child(Parent):
	def displayChild(self):
		print("This display belongs to child")
	def display(self):
		print("This display overrides parent class display")

		
>>> obj = Child()
>>> obj.display()
This display overrides parent class display
>>> class GrandChild(Child):
	def disp(self):
		print("This disp belongs to GrandChild")

		
>>> obj_1 = GrandChild()
>>> obj_1.display()
This display overrides parent class display
>>> class Parent():
	def display(self):
		print("This display belongs to parent")
	def show(self):
		print("This show function belongs to parent")

		
>>> obj_1 = GrandChild()
>>> 
