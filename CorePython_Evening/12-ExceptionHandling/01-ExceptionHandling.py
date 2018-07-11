# a = 10
# b = 0

try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a+b)
    print(a/b)
# except Exception as ex:
#     print(ex)
except (ValueError, ZeroDivisionError) as err:
    print(err)
