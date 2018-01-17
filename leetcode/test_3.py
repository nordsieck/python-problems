import unittest

class Solution:
    def lengthOfLongestSubstring(self, s):
        longest, first = 0, 0
        word = set()

        for ch in s:
            if ch in word:
                while True:
                    word.remove(s[first])
                    first += 1
                    if ch == s[first-1]:
                        break

            word.add(ch)
            if len(word) > longest:
                longest = len(word)

        return longest

class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring('dvdf'), 3)

if __name__ == '__main__':
    unittest.main()

        

        
