import time
import threading
import multiprocessing

def counter(num):
    init = 0
    while init < num:
        init += 1

    start = time.perf_counter()

    a = multiprocessing.Process(target=counter, args=(12500000000,))
    b = multiprocessing.Process(target=counter, args=(12500000000,))
    c = multiprocessing.Process(target=counter, args=(12500000000,))
    d = multiprocessing.Process(target=counter, args=(12500000000,))
    e = multiprocessing.Process(target=counter, args=(12500000000,))
    f = multiprocessing.Process(target=counter, args=(12500000000,))
    g = multiprocessing.Process(target=counter, args=(12500000000,))
    h = multiprocessing.Process(target=counter, args=(12500000000,))

    print(multiprocessing.cpu_count())
    end = time.perf_counter()
    print("It is done in:",int(end - start),"Seconds")

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

if __name__ == '__main__':
    main()