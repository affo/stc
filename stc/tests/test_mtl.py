from unittest import TestCase
from stc.mtl import *

class MTLOperatorsTestCase (TestCase):
    def setUp (self):
        self.trace = ['p', 'p', '', 'q', '', 'pq', '', 'pq', 'q', 'q']
        self.p = ap('p', self.trace)

    def test_eventually (self):
        expected = [True] * 5 + [False] * 5
        real = eventually(self.p, [3, 7])
        self.assertItemsEqual(real, expected)

    def test_eventually_with_zero_length_interval (self):
        expected = self.p
        real = eventually(self.p, [0, 0])
        self.assertItemsEqual(real, expected)

    def test_marcello_and_srdjan (self):
        simple = eventually(self.p, [3, 7])
        comp = oor(eventually(self.p, [3, 4]), eventually(eventually(self.p, [0, 3]), [4, 4]))
        self.assertItemsEqual(simple, comp)

    def test_next_equivalences (self):
        N = 100
        p = self.p
        base = nnext(p, [0, N])
        self.assertItemsEqual(base, nnext(p, [1, N]))
        self.assertItemsEqual(base, nnext(p, [1, 1]))

    def test_globally (self):
        ap = [False, False, True, False, True, True, True, False, False, False]
        interval = [2, 4]
        expected = [False, False, True] + [False] * 5 + [True, True]
        real = globally(ap, interval)
        self.assertItemsEqual(expected, real)

