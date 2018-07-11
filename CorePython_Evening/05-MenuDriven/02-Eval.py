def calculator(x,y, opr):
    # if ch == "1":
    #     return x + y
    # elif ch == "2":
    #     return x - y
    return eval(x+opr+y)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

user_choice = input("Enter your choice : ")

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

result = 0

todo = {
    "1" : "+",
    "2" : "-",
    "3" : "*",
    "4" : "/"
}

# todo.get(user_choice)(num_1, num_2, user_choice)
opr = todo.get(user_choice)
print(calculator(num_1, num_2, opr))
