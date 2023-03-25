import xc3


def exp():
    for i in range(26):
        t = xc3.XC3(i)
        print(f'In a tree of degree {i}, there are', '{:,}'.format(t.nodes()), 'node(s)')


if __name__ == '__main__':
    exp()
