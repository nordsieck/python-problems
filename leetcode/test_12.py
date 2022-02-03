import unittest
from typing import *

class Solution:

    # 3999 >= num >= 1
    def intToRoman(self, num: int) -> str:
        result = []
 
        conditions = [[1000, "M"],
                      [900, "CM"],
                      [500, "D"],
                      [400, "CD"],
                      [100, "C"],
                      [90, "XC"],
                      [50, "L"],
                      [40, "XL"],
                      [10, "X"],
                      [9, "IX"],
                      [5, "V"],
                      [4, "IV"],
                      [1, "I"],
        ]

        for val, rom in conditions:
            while num >= val:
                num -= val
                result.append(rom)

        return "".join(result)

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[1, "I"],
                [3, "III"],
                [4, "IV"],
                [14, "XIV"],

                [3, "III"],
                [58, "LVIII"],
                [1994, "MCMXCIV"],
        ]

        for a, b in data:
            self.assertEqual(s.intToRoman(a), b)
