from threading import Thread

def sub_function():
    print("Start the sub process")
    for i in range(20):
        print("sub",i)
    print("Exit sub")

def main_function():
    print("Start the thread")
    t_1 = Thread(target = sub_function)
    t_1.start() 
    for i in range(10):
        print("main",i)
    print("Exit main")

th_1 = Thread(target=main_function)
th_1.start()