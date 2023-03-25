import xc3


def exp():
    for i in range(26):
        t = xc3.XC3(i)
        print(f'XC3 Tree of degree {i} has a height of {t.height()}')


def graph():
    y = []
    for i in range(26):
        t = xc3.XC3(i)
        y.append(t.height())
    return y


if __name__ == '__main__':
    exp()
