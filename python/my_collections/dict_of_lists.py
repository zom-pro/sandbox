from pprint import pprint
from _collections import defaultdict


def dict_of_lists_old(sample):
    d = {}
    for k, v in sample:
        if k not in d.keys():
            d[k] = []
        d[k].append(v)
    return d

def dict_of_lists(sample):
    d = defaultdict(list)
    for k, v in sample:
        d[k].append(v)
    return d