try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a+b)
    print(a/b)
# except (ValueError, ZeroDivisionError) as err:
#     print(err)
finally:
    print("I will always execute")

print("Let me execute")
