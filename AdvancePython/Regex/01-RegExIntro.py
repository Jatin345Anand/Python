import re

str_1 = "A quick brown fox jumps over the lazy dog"
str_2 = "Salary of Ram is 12000 and Salary of Shyam is 15000"

# search will return object of first occurrence
# search = re.search('([a-z]\w+)', str_1)

# will return list of all matching words
search = re.findall('([a-z]\w+)', str_1)
print(search)

search = re.findall('([A-Z]\w+ | [0-9]\w+)', str_2)
print(search)