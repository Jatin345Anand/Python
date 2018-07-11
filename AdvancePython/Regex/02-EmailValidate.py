import re

pattern = '([a-z | 0-9]\w+([.]\w+)|(\w+))([@]\w+([. | -]\w+)+|([.]\w+))'

email_id = input("Enter emailID : ")

if re.match(pattern, email_id):
    print("Email Valid")
else:
    print("Invalid")