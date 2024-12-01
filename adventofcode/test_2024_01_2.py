import sys
import unittest
from typing import *

def main():
    s = Solution()

    with open(sys.argv[1], "r") as file:
        for line in file:
            pass

class Solution:
    pass

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [
        ]

        for a, b in data:
            self.assertEqual(s.fn(a), b)

if __name__ == "__main__":
    main()
