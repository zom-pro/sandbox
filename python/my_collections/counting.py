from pprint import pprint
from _collections import defaultdict

def counting_appearance_old(sample):
    d = {}
    for key in sample:
        if key not in d.keys():
            d[key] = 0
        d[key] += 1
    return d

def counting_appearance(sample):
    d = defaultdict(int)
    for k in sample:
        d[k] += 1
    return d
