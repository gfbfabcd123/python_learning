import threading
import time
class MyTheard(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)
    def run(self):
        print("get detail")
        time.sleep(2)
        print("get end")
if __name__ == '__main__':
    t1=MyTheard("haha")
    print(t1.name)
    t1.start()
    t1.join()
    print("end")