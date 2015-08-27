from _collections import deque
from timeit import timeit
import itertools

from pdb import set_trace as debug

def old_moving_average(iterable, n=3):
    len_iterable = len(iterable)
    for e, i in enumerate(iterable):
        # necessary to stop it before reaches the end.
        if e <= len_iterable - n:
            yield sum(iterable[e:n + e]) / n

def moving_average(iterable, n=3):
        it = iter(iterable)
        d = deque(itertools.islice(it, n - 1))
        d.appendleft(0)
        s = sum(d)
        for elem in it:
            s += elem - d.popleft()
            d.append(elem)
            yield s / n
     
def create_run(iterable_length):
    mas = moving_average(range(iterable_length))
    for ma in mas:
        ma * 2

def create_run_old(iterable_length):
    mas = old_moving_average(range(iterable_length))
    for ma in mas:
        ma * 2

if __name__ == '__main__':
    for i in (100, 1000, 10000, 100000):
        print("Length deque: ", i, timeit("create_run(" + str(i) + ")",
                                          "from __main__ import create_run", number=1000))
        print("Length normal: ", i, timeit("create_run_old(" + str(i) + ")",
                                           "from __main__ import create_run_old", number=1000))
        print('\n')
