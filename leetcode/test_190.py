import unittest
from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        LEN, result = 32, 0
        for _ in range(LEN - 1):
            if n % 2 == 1: result += 1
            result, n = result << 1, n >> 1

        if n % 2 == 1: result += 1
        return result

    def two(self, n: int) -> int:
        LEN = 32
        for i in range(int(LEN / 2)):
            bot, top = (n >> i) & 1, (n >> LEN - i - 1) & 1
            if top == bot: continue
                
            if top == 1:
                n ^= 1 << LEN - i - 1
            else:
                n |= 1 << LEN - i - 1

            if bot == 1:
                n ^= 1 << i
            else:
                n |= 1 << i

        return n
                 

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[0, 0],
                [0b00000000000000000000000000000001,
                 0b10000000000000000000000000000000],
                [0b10000000000000000000000000000000,
                 0b00000000000000000000000000000001],
                [0b10000000000000000000000000000001,
                 0b10000000000000000000000000000001],
                [0b01010101010101010101010101010101,
                 0b10101010101010101010101010101010],
                [0b00000010100101000001111010011100, 964176192],
                [0b11111111111111111111111111111101, 3221225471],
        ]

        for a, b in data:
            self.assertEqual(s.reverseBits(a), b)

    def testN(self):
        s = Solution()
        
        data = [[0, 0],
                [0b00000000000000000000000000000001,
                 0b10000000000000000000000000000000],
                [0b10000000000000000000000000000000,
                 0b00000000000000000000000000000001],
                [0b10000000000000000000000000000001,
                 0b10000000000000000000000000000001],
                [0b01010101010101010101010101010101,
                 0b10101010101010101010101010101010],
                [0b00000010100101000001111010011100, 964176192],
                [0b11111111111111111111111111111101, 3221225471],
        ]
        for a, b in data:
            self.assertEqual(s.two(a), b)
