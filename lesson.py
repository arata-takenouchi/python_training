import threading
from multiprocessing import (
    Process,
    Lock, RLock, Semaphore, Queue, Event, Condition, Barrier,
    Value, Array, Pipe, Manager
)

import concurrent.futures
import logging
import multiprocessing
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker(x, y):
    logging.debug('start')
    time.sleep(3)
    r = x * y
    logging.debug(r)
    logging.debug('end')
    return r

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # f1 = executor.submit(worker, 2 , 5)
        # f2 = executor.submit(worker, 2 , 5)
        # logging.debug(f1.result())
        # logging.debug(f2.result())

        args = [[2, 2], [5, 5]]
        r = executor.map(worker, *args)
        logging.debug(r)
        logging.debug([i for i in r])

if __name__ == '__main__':
    main()
