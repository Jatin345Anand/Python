def parent(x):
    def child():
        print("This is parent function...")
        return x

    return child

# Decorator
@parent
def anotherFunc():
    print("This is another function...")

a = anotherFunc()
a()

