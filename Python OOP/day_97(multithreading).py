import threading
import time
from concurrent.futures import ThreadPoolExecutor
"""Indicates some task being done"""


def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    pass


time1 = time.perf_counter()

"""Normal code"""
# fun(3)
# fun(2)
# fun(1)


"""Code using threads"""
t1 = threading.Thread(target=fun, args=[3])
t2 = threading.Thread(target=fun, args=[2])
t3 = threading.Thread(target=fun, args=[1])

"""TO indicate to start"""
t1.start()
t2.start()
t3.start()

"""Will start when one is completed"""
t1.join()
t2.join()
t3.join()

"""Calculating the time"""
time2 = time.perf_counter()
print(time2 - time1)


def pooling_demo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future = executor.submit(fun, 3)
        # print(future.result())
        # future = executor.submit(fun, 2)
        # print(future.result())
        # future = executor.submit(fun, 4)
        # print(future.result())
        l = [3, 5, 1, 2]
        results = executor.map(fun, l)
        for result in results:
            print(result)


pooling_demo()


"""Code with Harry's code"""

