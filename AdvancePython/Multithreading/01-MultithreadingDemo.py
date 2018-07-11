import threading
import time

def job():
    print("{} enters".format(threading.current_thread().getName()))
    time.sleep(2)
    for i in range(10):
        print("Value of i is",i)

    print("{} exits".format(threading.current_thread().getName()))

worker = threading.Thread(target=job, name="Thread_1")
worker_2 = threading.Thread(target=job, name="Thread_2")

worker.start()
worker_2.start()

# Main Thread
print(threading.current_thread().getName())