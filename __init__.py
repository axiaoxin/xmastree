#!/usr/bin/env python
from random import randint


class XmasTree(object):

    def __init__(self, height=20, center=80):
        self.height = height
        self.center = center

    def _ornament(self):
        if randint(0, 99) > 80:
            return "!@#$%^&"[randint(0, 6)]
        else:
            return ' '

    def _bough(self, n, last=False):
        first = '/' + "".join([self._ornament() for m in range(0, n * 2 - 1)]) + '\\'
        if last:
            second = '/' + '_' * (n * 2 + 1) + '\\'
        else:
            second = '/' + "".join([self._ornament() for m in range(0, n * 2 - 1)]) + '\\'
        return [first, second]

    def _tree(self):
        return (['*'] +
                sum([self._bough(n) for n in range(1, (self.height - 1) // 2)], []) +
                self._bough((self.height - 1) // 2, True) +
                ['| |'])

    def show(self):
        print '\n'.join([s.center(self.center)
                         for s in self._tree()])

if __name__ == '__main__':
    tree = XmasTree()
    tree.show()
