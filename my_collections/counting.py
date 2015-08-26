from pprint import pprint
from _collections import defaultdict
sample = [2, 1, 2, 3, 3, 2, 3, 1, 2, 3, 1, 1]

def counting_appearance():
    d = {}
    for key in sample:
        if key not in d.keys():
            d[key] = 0
        d[key] += 1
    return d

def counting_appearance_alternative():
    d = defaultdict(int)
    for k in sample:
        d[k] += 1
    return d

if __name__ == '__main__':
    d = counting_appearance()
    print(list(d.items()))

    d = counting_appearance_alternative()
    print(list(d.items()))