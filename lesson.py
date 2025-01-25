import logging
import queue
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1(condition):
    with condition:
        condition.wait()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

def worker2(condition):
    with condition:
        condition.wait()
        logging.debug('start')
        time.sleep(3)
        logging.debug('end')

def worker3(condition):
    with condition:
        logging.debug('start')
        logging.debug('end')
        condition.notifyAll()

if __name__ == '__main__':
    event = threading.Condition()
    t1 = threading.Thread(target=worker1, args=(event,))
    t2 = threading.Thread(target=worker2, args=(event,))
    t3 = threading.Thread(target=worker3, args=(event,))
    t1.start()
    t2.start()
    t3.start()
