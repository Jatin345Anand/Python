def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_choice = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

result = 0

if user_choice == "1":
    add(num_1, num_2)
elif user_choice == "2":
    sub(num_1, num_2)
elif user_choice == "3":
    div(num_1, num_2)
elif user_choice == "4":
    mul(num_1, num_2)
