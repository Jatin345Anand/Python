import threading
import time

def job(x):
    print("Worker_1",x)
    print("{} enters".format(threading.current_thread().getName()))
    for i in range(10):
        print("Value of i is",i)

    print("{} exits".format(threading.current_thread().getName()))

def job_2(x):
    print("Worker_2", x)
    print("{} enters".format(threading.current_thread().getName()))
    for i in range(10):
        print("Value of i is", i)

    print("{} exits".format(threading.current_thread().getName()))

worker = threading.Thread(target=job, args=(5,), name="Thread_1")
worker_2 = threading.Thread(target=job_2, args=(2,), name="Thread_2")

# job()
# job_2()

worker.start()
worker_2.start()