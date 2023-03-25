class XC3:
    def __init__(self, degree):
        self.degree = degree
        self.children = []
        for i in range(1, degree + 1):
            self.children.append(XC3(i - 2 if i > 2 else 0))

    def height(self):
        if not self.children:
            return 1
        height = 2
        last_child = self.children[-1]
        while last_child and last_child.children:
            height += 1
            last_child = last_child.children[-1]
        return height

    def nodes(self):
        if not self.children:
            return 1
        return 1 + sum([child.nodes() for child in self.children])
