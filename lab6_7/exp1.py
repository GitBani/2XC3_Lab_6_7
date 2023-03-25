import rbt
import bst
from random import randint

L = 10_000


def create_random_list(length):
    return [randint(-100, 100) for _ in range(length)]


# takes about 10 seconds to run
def exp():
    differences = []
    for _ in range(100):
        li = create_random_list(L)
        r = rbt.RBTree()
        b = bst.BST()
        for val in li:
            r.insert(val)
            b.insert(val)
        differences.append(b.get_height() - r.get_height())
    print(differences)
    return sum(differences) / len(differences)


if __name__ == '__main__':
    print(exp())
