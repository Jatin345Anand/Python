try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a+b)
    print(a/b)
except (ValueError, ZeroDivisionError) as err:
    print(err)

else:
    print("Inside else block")

finally:
    print("I will always execute")

print("Let me execute")
