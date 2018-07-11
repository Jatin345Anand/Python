a,b,c = 11,14,20

if a > b and a > c:
    print("A is greater")
elif b > c and b > a:
    print("B is greater")
else:
    print("C is greater")


if a > b or a > c:
    print("A is greater")
elif b > c or b > a:
    print("B is greater")
else:
    print("C is greater")
