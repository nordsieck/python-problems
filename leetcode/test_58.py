import unittest
from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        while i >= 0:
            if s[i] == " ":
                if count != 0: break
            else:
                count += 1
            i -= 1

        return count

            

class TestSolution(unittest.TestCase):
    def test_fn(self):
        s = Solution()
        data = [["Hello World", 5],
                ["    fly me   to    the moon  ", 4],
                ["luffy is still joyboy", 6],
                ["a", 1],
        ]

        for a, b in data:
            self.assertEqual(s.lengthOfLastWord(a), b)
