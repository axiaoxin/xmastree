#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from random import choice
from termcolor import colored
from termcolor import COLORS

HEIGHT = 20
CENTER = 80
GREETING = "Merry Xmas! Blessing comes from @阿小信大人."
ORNAMENT = "!@#$%^&"

class XmasTree(object):

    def __init__(self, height=HEIGHT, center=CENTER, greeting=GREETING, ornament=ORNAMENT, blink=True):
        self.height = height
        self.center = center
        self.greeting = greeting
        self.ornament = ornament
        self.blink = blink
        self._new_tree()

    def _ornament(self):
        if randint(0, 99) > 80:
            return choice(self.ornament)
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
        if self.blink:
            for i in self.ornament:
                self.tree = self.tree.replace(i, colored(i, choice(COLORS.keys()), attrs=['blink', 'bold']))
                if randint(0, 99) > 50:
                    self.tree = self.tree.replace(i, colored(choice(self.ornament), choice(COLORS.keys()), attrs=['blink', 'bold']))
            self.tree = self.tree.replace('/', colored('/', 'green', attrs=['bold'])).replace('\\', colored('\\', 'green', attrs=['bold']))
            self.tree = self.tree.replace('*', colored('*', 'green', attrs=['bold'])).replace('_', colored('_', 'green', attrs=['bold']))
            self.tree = self.tree.replace('|', colored('|', 'green', attrs=['bold']))

    def show(self):
        print self.tree
        print
        print colored(self.greeting.center(self.center), 'red', attrs=['bold', 'reverse', 'underline'])

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Xmas Tree")
    parser.add_argument("--height", '-H',
                        help="tree height",
                        type=int,
                        default=HEIGHT,
                        dest="height")
    parser.add_argument("--center", '-C',
                        help="tree center",
                        type=int,
                        default=CENTER,
                        dest="center")
    parser.add_argument("--greeting", '-G',
                        help="greeting words",
                        type=str,
                        default=GREETING,
                        dest="greeting")
    parser.add_argument("--ornament", '-O',
                        help="ornaments",
                        type=str,
                        default=ORNAMENT,
                        dest="ornament")
    parser.add_argument("--no-blink", '-B',
                        help="colorful blinking",
                        default=True,
                        action="store_false",
                        dest="blink")
    args = parser.parse_args()
    tree = XmasTree(args.height, args.center, args.greeting, args.ornament, args.blink)
    tree.show()

if __name__ == '__main__':
    main()
