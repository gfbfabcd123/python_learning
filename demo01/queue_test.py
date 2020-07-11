import threading
import time
from queue import Queue

urllsit=[]
def add_detail(urllsit):
    while True:
        urllsit.append("haha")
        time.sleep(2)
        print("addddd")
def get_detail(urllsit):
    while True:
        if len(urllsit):
            src=urllsit.pop()
            print(src)
            time.sleep()

    print("get {} end \n".format(url))
if __name__=="__main__":
    queue=Queue(maxsize=1000)
    # task_done join