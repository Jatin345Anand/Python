import urllib.request

page = urllib.request.urlopen('https://www.google.co.in')
data = page.read()
# print(data)

with open('google.html', 'wb') as file:
    file.write(data)
    print("Data Written...")