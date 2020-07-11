# gil使得同一时间只有一个线程在一个cpu上捃行字节码
# 编译字节码
"""
import dis
def add(a):
    a=a+1
    return a
print(dis.dis(add))
"""
import threading

total=0
lock=threading.Lock()
def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total+=1
        lock.release()
def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total-=1
        lock.release()
if __name__ == '__main__':
    ## 死锁问题  rlock
    t1=threading.Thread(target=add)
    t2=threading.Thread(target=desc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(total)




