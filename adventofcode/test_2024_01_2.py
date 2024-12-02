import functools
import sys
import unittest
from typing import *

def main():
    s = Solution()
    a = []
    b = {}

    with open(sys.argv[1], "r") as file:
        for line in file:
            l = line.split()
            a.append(int(l[0]))
            val = int(l[1])
            if not val in b:
                b[val] = 1
            else:
                b[val] += 1

    print(s.similarity(a, b))

class Solution:
    def similarity(self, a: List[int], b: Dict[int, int]) -> int:
        return functools.reduce(lambda acc, e: acc + e * b.get(e, 0), a, 0)

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
            [[1], {1:1}, 1],
            [[1, 1], {1:1}, 2],
            [[1], {2:1}, 0],
            [[3, 4, 2, 1, 3, 3], {3:3, 4:1, 5:1, 9:1}, 31],
        ]

        for a, b, sim in data:
            self.assertEqual(s.similarity(a, b), sim)

if __name__ == "__main__":
    main()
