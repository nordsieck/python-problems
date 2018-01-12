import unittest

class Solution:
    def anagramMappings( self, A, B ):
        mapping = {val:idx for idx, val in enumerate(B)}
        return [mapping[val] for val in A]

class TestSolution(unittest.TestCase):
    def test_anagramMappings(self):
        am = Solution().anagramMappings
        self.assertEqual(am([11, 12, 13, 14], [14, 11, 13, 12]), [1, 3, 2, 0])

if __name__ == '__main__':
    unittest.main()
