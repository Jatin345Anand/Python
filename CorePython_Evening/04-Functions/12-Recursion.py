def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("Factorial of ", num, "is", factorial(num))

# def game():
#     x = 10
#     while True:
#         print("Game is going on...")
#         x -= 1
#
#         if x == 0:
#             print("Game Over")
#             game()
#
# game()
