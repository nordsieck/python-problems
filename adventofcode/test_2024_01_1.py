import sys
import unittest
from typing import *

def main():
    s = Solution()
    a = []
    b = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            l = line.split()
            a.append(int(l[0]))
            b.append(int(l[1]))
    print(s.distance(a, b))

class Solution:
    def distance(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()

        return sum([abs(i-j) for i, j in zip(a, b)])

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
            [[1], [2], 1],
            [[1, 2, 3], [5, 6, 7], 12],
        ]

        for a, b, d in data:
            self.assertEqual(s.distance(a, b), d)

if __name__ == "__main__":
    main()
