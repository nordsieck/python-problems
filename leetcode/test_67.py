import unittest
from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = [ord(v) - ord("0") for v in list(a)]
        B = [ord(v) - ord("0") for v in list(b)]

        if len(A) < len(B): A, B = B, A
        
        i, j = len(A) - 1, len(B) - 1

        carry = 0
        while i >= 0 and j >= 0:
            A[i] += B[j] + carry
            carry = int(A[i] / 2)
            A[i] = A[i] % 2
            i, j = i - 1, j - 1

        while i >= 0:
            A[i] += carry
            carry = int(A[i] / 2)
            A[i] = A[i] % 2
            i -= 1

        if carry == 1: A.insert(0, 1)

        return "".join([chr(v + ord("0")) for v in A])

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [["0", "0", "0"],
                ["0", "1", "1"],
                ["1", "1", "10"],
                ["11", "1", "100"],
                ["1010", "1011", "10101"],
                ["1", "111", "1000"],
        ]

        for a, b, sol in data:
            self.assertEqual(s.addBinary(a, b), sol)
