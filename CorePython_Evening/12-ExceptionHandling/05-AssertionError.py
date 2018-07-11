def division(a,b):
    try:
        c = a - b
        # User Defined Exception
        assert (c > 0), "Difference should be greater than or equals to zero"
        print("Value of c",c)
    except AssertionError as err:
        print(err)

division(5,12)
