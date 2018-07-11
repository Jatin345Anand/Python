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
    result = num_1 + num_2
    print(result)
elif user_choice == "2":
    result = num_1 - num_2
    print(result)
elif user_choice == "3":
    result = num_1/num_2
    print(result)
elif user_choice == "4":
    result = num_1 * num_2
    print(result)
