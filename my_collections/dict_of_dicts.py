from pprint import pprint
from _collections import defaultdict
sample = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

def dict_of_lists():
    d = {}
    for k, v in sample:
        if k not in d.keys():
            d[k] = []
        d[k].append(v)
    return d

def dict_of_lists_alternative():
    d = defaultdict(list)
    for k, v in sample:
        d[k].append(v)
    return d

if __name__ == '__main__':
    d = dict_of_lists()
    print(list(d.items()))

    d = dict_of_lists_alternative()
    print(list(d.items()))