import unittest
from typing import *

class Solution:
    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]: return False
            i, j = i + 1, j - 1
        return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if self.isPalindrome(words[i]): return words[i]
        return ""


class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[["def", "ghi"], ""],
                [["notapalindrome", "racecar"], "racecar"],
                [["abc", "car", "ada", "racecar", "cool"], "ada"],
        ]

        for a, b in data:
            self.assertEqual(s.firstPalindrome(a), b)
