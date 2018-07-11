def division(a,b):
    try:
        c = a - b
        # Raising Exceptions on run time
        if c < 0:
            raise ValueError("Difference should be greater than or equals to zero")
        else:
            print("Value of c",c)
    except ValueError as err:
        print(err)

division(5,12)
