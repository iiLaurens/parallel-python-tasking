from multiprocessing.dummy import Process, Manager
from time import sleep
import sys
from functools import wraps
import petname

def error_catching(func):
    """ Catch and handle errors in a process
    """
    @wraps(func) #wraps allows pickling of decorators
    def my_func(*args, **kwargs):
        process_number = petname.Generate(2,'-')
        while True:
            try:
                return func(process_number, *args, **kwargs)
            except KeyboardInterrupt:
                print("Keyboard interrupt in worker", process_number)
                return
            except Exception as e:
                print("Error in worker {}:\n\t{}\n\tRestarting in 3 seconds...".format(process_number, repr(e)))
                sleep(3)
    return my_func


@error_catching
def f(process_number):
    print("starting worker:", process_number)
    while True:
        sleep(2)
        print("Worker {} checks in.".format(process_number))


if __name__ == '__main__':
    processes = []
    manager = Manager()

    for i in range(3):
        p = Process(target=f)
        p.daemon = True
        p.start()
        processes.append(p)

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt in main")
        sys.exit()
