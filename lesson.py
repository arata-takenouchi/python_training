import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(barrier):
    r = barrier.wait()
    logging.debug(f'num={r}')
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

def worker2(barrier):
    r = barrier.wait()
    logging.debug(f'num={r}')
    while True:
        logging.debug('start')
        time.sleep(2)
        logging.debug('end')

if __name__ == '__main__':
    event = threading.Barrier(2)
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t1.start()
    t2.start()
