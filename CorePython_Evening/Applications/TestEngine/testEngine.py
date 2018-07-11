# Check if ans is right or wrong
# prize include

options = [
    ['Lalu', 'Modi', 'Arvind', 'Yogi'],
    ['England','Spain','Italy','Brazil']
]
prize = [1000, 2000, 5000, 10000, 20000]
with open('questions.txt', 'r') as file:
    for i in range(5):
        data = file.readline()
        print(data)
        opt = options[i]
        for j in opt:
            print(j)
        ans = input("\nYour Ans : ")
        print("Correct Ans")
