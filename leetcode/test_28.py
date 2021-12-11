import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0: return 0
        return haystack.find(needle)
        
class TestSolution(unittest.TestCase):
    def test_strStr_empty(self):
        s = Solution()
        self.assertEqual(s.strStr("", ""), 0)
        self.assertEqual(s.strStr("a", ""), 0)

    def test_strStr_missing(self):
        s = Solution()
        self.assertEqual(s.strStr("a", "aa"), -1)
        self.assertEqual(s.strStr("a", "b"), -1)

    def test_strStr_found(self):
        s = Solution()
        self.assertEqual(s.strStr("aaa", "aaa"), 0)
        self.assertEqual(s.strStr("baaa", "aaa"), 1)
        self.assertEqual(s.strStr("aaaa", "aaa"), 0)
