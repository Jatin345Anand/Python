def parent(x):
    print("This is parent function...")
    x()

def anotherFunc():
    print("This is another function...")


parent(anotherFunc)
