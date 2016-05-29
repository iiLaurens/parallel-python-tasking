from multiprocessing.dummy import Pool, Process, Manager
import time


def f(process_number):
    print("starting thread: ", process_number)
    while True:
        print(process_number)
        time.sleep(1)

if __name__ == '__main__':
    Process(target=f,args=(1,)).start()

    pool = Pool(3)
    pool.apply_async(f,(2,))
    while True:
        time.sleep(2)
