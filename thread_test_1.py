from threading import Thread
import time

def sub_function(number):
    print("Start the sub process", number)
    for i in range(20):
        print(number, "sub",i)
    print("Exit sub")

for i in range(5):
    t = Thread(target= sub_function(i))
    t.start()
    # time.sleep(0.1)

