# Closures/Nested Functions

# def outer(m):
#     message = m
#
#     def inner():
#         print("Message is",message)
#
#     inner()
#
# outer("Hello world...")

def outer(m):
    def inner():
        print("I am inner function")
        return m+1
    return inner

# print(outer(10))
a = outer(2)
print(a())
