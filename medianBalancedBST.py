from collections.abc import Iterable


class MedianBalancedBST:
    def __init__(self, elements=None):
        self.data = None
        self.left = None
        self.right = None
        self._balance_factor = 0
        if elements is not None:
            if isinstance(elements, Iterable):
                for element in elements:
                    self.add_element(element)
            else:
                self.data = elements

    def _add_left(self, element):
        if self.left is None:
            self.left = MedianBalancedBST(element)
        else:
            self.left.add_element(element)

    def _add_right(self, element):
        if self.right is None:
            self.right = MedianBalancedBST(element)
        else:
            self.right.add_element(element)

    def add_element(self, element):
        if self.data is None:
            self.data = element
        else:
            if element < self.data:
                self._add_left(element)
                self._balance_factor += 1
            else:
                self._add_right(element)
                self._balance_factor -= 1
            self.maybe_balance_tree()

    def maybe_balance_tree(self):
        if self._balance_factor > 1:
            if self.left.right is not None:
                new_root = self.left.pop_most_right()
            else:
                new_root = self.left.data
                self.left = self.left.left
            self._add_right(self.data)
            self.data = new_root
            self._balance_factor -= 2
        elif self._balance_factor < 0:
            if self.right.left is not None:
                new_root = self.right.pop_most_left()
            else:
                new_root = self.right.data
                self.right = self.right.right
            self._add_left(self.data)
            self.data = new_root
            self._balance_factor += 2

    def median(self):
        if self.data is None:
            return None
        if self._balance_factor == 0:
            return self.data
        return (self.data + self.left.get_most_right()) / 2.0

    def pop_most_left(self):
        if self.left.left is None:
            most_left = self.left.data
            self.left = self.left.right
        else:
            most_left = self.left.pop_most_left()
        self._balance_factor -= 1
        self.maybe_balance_tree()
        return most_left

    def pop_most_right(self):
        if self.right.right is None:
            most_right = self.right.data
            self.right = self.right.left
        else:
            most_right = self.right.pop_most_right()
        self._balance_factor += 1
        self.maybe_balance_tree()
        return most_right

    def get_most_right(self):
        return self.data if self.right is None else self.right.get_most_right()
