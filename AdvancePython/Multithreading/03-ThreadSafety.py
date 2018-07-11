import threading
import time

class Job():

    def __init__(self):
        self.total_bal = 12000

    def atm(self,amount):
        # total_bal = 12000
        lock.acquire()
        print("{} enters".format(threading.current_thread().getName()))
        print("Lock acquired by", threading.current_thread().getName())
        time.sleep(2)
        if amount < self.total_bal:
            self.total_bal -= amount
            print("Amount withdraw successfully by...",threading.current_thread().getName())
            print("Remaining Amount is",self.total_bal)
        else:
            print("Not Sufficient Balance")

        print("{} exits".format(threading.current_thread().getName()))
        print("Lock released by", threading.current_thread().getName())
        lock.release()

job = Job()

lock = threading.Lock()

thread_1 = threading.Thread(target=job.atm, args=(4000,), name='Ram')
thread_2 = threading.Thread(target=job.atm, args=(4000,), name='Shyam')

thread_1.start()
thread_2.start()