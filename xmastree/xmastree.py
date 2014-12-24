#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from termcolor import colored

class XmasTree(object):

    def __init__(self, height=20, center=80, greeting="Merry Xmas!"):
        self.height = height
        self.center = center
        self.greeting = greeting
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
        self.boughs = (['*'] +
                          sum([self._bough(n)
                               for n in range(1, (self.height - 1) // 2)], []) +
                          self._bough((self.height - 1) // 2, True) + ['| |'])
        self.tree = '\n'.join([s.center(self.center)
                               for s in self.boughs])

    def show(self):
        print colored(self.tree, 'green', attrs=['bold'])
        print colored(self.greeting, 'red', attrs=['bold', 'blink', 'reverse', 'underline'])


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Xmas Tree")
    parser.add_argument("--height", '-H',
                        help="tree height",
                        type=int,
                        default=20,
                        dest="height")
    parser.add_argument("--center", '-C',
                        help="tree center",
                        type=int,
                        default=80,
                        dest="center")
    parser.add_argument("--greeting", '-G',
                        help="greeting words",
                        type=str,
                        default='Merry Xmas!',
                        dest="greeting")
    args = parser.parse_args()
    tree = XmasTree(args.height, args.center, args.greeting)
    tree.show()

if __name__ == '__main__':
    main()
