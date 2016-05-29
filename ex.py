from multiprocessing.dummy import Process, Manager, Pool
from time import sleep

def f(process_number):
    # print("starting thread: ", process_number)
    # while True:
    #     print(process_number)
    #     sleep(1)
    try:
        print("starting thread: ", process_number)
        while True:
            print(process_number)
            sleep(3)
    except KeyboardInterrupt:
        print("Keyboard interrupt in process: ", process_number)
    finally:
        print("cleaning up thread", process_number)

if __name__ == '__main__':

    #pool = Pool(3)

    #pool.apply_async(f,(2,))

    processes = []
    for i in range(4):
        p = Process(target=f, args=(i,))
        p.start()
        processes.append(p)

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Keyboard interrupt in main")
    finally:
        print("Cleaning up Main")
