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
3. Mul
4. Div
""")

user_choice = input("Enter your choice : ")

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

result = 0

todo = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div
}

todo.get(user_choice)(num_1, num_2)
