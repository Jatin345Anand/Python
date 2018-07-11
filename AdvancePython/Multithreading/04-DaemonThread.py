import threading

def job_1():
    print("{} enters".format(threading.current_thread().getName()))
    for i in range(100000):
        for j in range(500):
            i + j
    print("{} exits".format(threading.current_thread().getName()))

def job_2():
    print("{} enters".format(threading.current_thread().getName()))
    for i in range(10000):
        for j in range(500):
            i + j
    print("{} exits".format(threading.current_thread().getName()))

thread_1 = threading.Thread(target=job_1)
thread_1.setDaemon(True)

thread_2 = threading.Thread(target=job_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()