class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() is None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        if not self.is_left_child() or not self.is_red():
            return
        # swap colours
        self.colour, self.parent.colour = self.parent.colour, self.colour
        # temp storage
        right_child = self.right
        grandparent = self.parent.parent
        if grandparent is not None:
            was_right = self.parent.is_right_child()
        # swaps
        self.right, self.parent = self.parent, self.parent.parent
        self.right.parent, self.right.left = self, right_child
        if right_child is not None:
            right_child.parent = self.right
        # if there was a grandparent, update its record of children
        if grandparent is not None:
            if was_right:
                grandparent.right = self
            else:
                grandparent.left = self

    def rotate_left(self):
        if not self.is_right_child() or not self.is_red():
            return
        # swap colours
        self.colour, self.parent.colour = self.parent.colour, self.colour
        # temp storage
        left_child = self.left
        grandparent = self.parent.parent
        if grandparent is not None:
            was_right = self.parent.is_right_child()
        # swaps
        self.left, self.parent = self.parent, self.parent.parent
        self.left.parent, self.left.right = self, left_child
        if left_child is not None:
            left_child.parent = self.left
        # if there was a grandparent, update its record of children
        if grandparent is not None:
            if was_right:
                grandparent.right = self
            else:
                grandparent.left = self


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right is None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def colour_swap(self, node):
        if node.left.is_red() and node.right.is_red():
            node.left.make_black()
            node.right.make_black()
            if node is not self.root:
                node.make_red()

    # An atrocity, sorry to whoever reads this
    def fix(self, node):
        # If single node, do nothing
        if node.parent is None:
            node.make_black()
        # iterate up tree to make fixes, if a node is black then properties should hold
        # (not in general, but considering that all other functions work)
        while node is not None and node.is_red():
            # case 1: red right child of a black node
            if node.parent.is_black() and node.is_right_child():
                # sub-case 1: rotation needed
                if node.get_brother() is None or node.get_brother().is_black():
                    node.rotate_left()
                    # if root was involved in the rotation, update root
                    if node.left == self.root:
                        self.root = node
                # sub-case 2 (node's brother is also red): colour swap is sufficient
                else:
                    self.colour_swap(node.parent)
            # case 2: parent is also red
            elif node.parent.is_red():
                # sub-case 1: node is a left child
                if node.is_left_child():
                    node.parent.rotate_right()
                    # if root was involved in the rotation, update root
                    if node.get_brother() == self.root:
                        self.root = node.parent
                    self.colour_swap(node.parent)
                # sub-case 2: node is right child
                else:
                    node.rotate_left()
                    node.rotate_right()
                    # if root involved in rotation, update it
                    if node.right == self.root:
                        self.root = node
                    self.colour_swap(node)
                    # skip to next iteration without updating node due to positioning
                    continue
            # if red node is left child of a black node, then nothing is wrong (assuming all other functions work)
            else:
                break
            # go up tree
            node = node.parent
        # potentially unnecessary, but just in case (also it was already provided in the function)
        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left is None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right is None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"
