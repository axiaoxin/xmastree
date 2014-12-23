#!/usr/bin/env python
__version__ = '0.0.1'

from random import randint


class XmasTree(object):

    def __init__(self, height=20, center=80):
        self.height = height
        self.center = center
        self._new_tree()

    def _ornament(self):
        if randint(0, 99) > 80:
            return "!@#$%^&"[randint(0, 6)]
        else:
            return ' '

    def _bough(self, n, last=False):
        first = '/' + "".join([self._ornament()
                               for _ in range(0, n * 2 - 1)]) + '\\'
        if last:
            second = '/' + '_' * (n * 2 + 1) + '\\'
        else:
            second = '/' + "".join([self._ornament()
                                    for _ in range(0, n * 2 - 1)]) + '\\'
        return [first, second]

    def _new_tree(self):
        self.tree_list = (['*'] +
                          sum([self._bough(n)
                               for n in range(1, (self.height - 1) // 2)], []) +
                          self._bough((self.height - 1) // 2, True) + ['| |'])
        self.tree = '\n'.join([s.center(self.center)
                               for s in self.tree_list])

    def show(self):
        print self.tree


if __name__ == '__main__':
    tree = XmasTree()
    tree.show()
