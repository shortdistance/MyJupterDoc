# --*--coding:utf-8 --*--
from __future__ import print_function

import threading
import time
mutex = threading.RLock()

def worker(i):
    if mutex.acquire(1):  
        print(i)
        time.sleep(1)
        print("AWAKE")
        mutex.acquire()
        mutex.release()
    
for i in xrange(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
print("closed")