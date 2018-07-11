def emp(id, name, *address):
    print("User id : {} User Name : {}".format(id, name))
    print("User Address : {}".format(address))


emp(101,'Ram', 'Home Address', 'Office Address', 'Friend Address')

emp(102,'Shyam', 'Home Address')

emp(103,'Mohan','Home Address','Office Address')
