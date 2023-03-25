import rbt
import bst
from matplotlib import pyplot as pp
from random import randint
from math import log10


L = 100
S = int(L * log10(L) / 2)
R = 1000


def create_random_list(length):
    return [randint(-100, 100) for _ in range(length)]


def create_near_sorted_list(length, swaps):
    li = create_random_list(length)
    li.sort()
    for _ in range(swaps):
        r1 = randint(0, length - 1)
        r2 = randint(0, length - 1)
        li[r1], li[r2] = li[r2], li[r1]
    return li


def exp(swaps, runs):
    diffs = []
    for i in range(swaps + 1):
        total_height_diff = 0
        for _ in range(runs):
            li = create_near_sorted_list(L, i)
            r = rbt.RBTree()
            b = bst.BST()
            for val in li:
                r.insert(val)
                b.insert(val)
            total_height_diff += b.get_height() - r.get_height()
        diffs.append(total_height_diff / runs)
    return diffs


if __name__ == '__main__':
    pp.title('Number of Swaps vs. Average Height Difference')
    pp.xlabel('No. of swaps')
    pp.ylabel('Average difference in height')
    pp.plot(exp(S, R))
    pp.show()
