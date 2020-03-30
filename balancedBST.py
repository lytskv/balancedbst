class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BalancedBST:
    def __init__(self, elements=None):
        self.root = None
        if elements is not None:
            for element in elements:
                self.add_element(element)

    def add_element(self, element):
        if self.root is None:
            self.root = BSTNode(element, BalancedBST(), BalancedBST())
        else:
            if element < self.root.value:
                self.root.left.add_element(element)
            elif element > self.root.value:
                self.root.right.add_element(element)

    def median(self):
        return self.root.value if self.root is not None else None
