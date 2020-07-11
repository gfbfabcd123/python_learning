import threading
import time

def get(url):
    print('get')
    time.sleep(2)
    print("get end")

def get2(url):
    print('get2')
    time.sleep(2)
    print("get2 end")
if __name__ == '__main__':
    t1=threading.Thread(target=get,args=("faef",))
    t2=threading.Thread(target=get2,args=("fffffffffffffff",))
    start=time.time()
    #设置守护线程 主线程关闭后就会强行结束
    t1.setDaemon(True)
    t1.start()
    t2.start()
    #join 会柱塞代码
    t1.join(
    )
    t1.join()
    total=time.time()-start
    print(total)