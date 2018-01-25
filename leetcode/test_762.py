import unittest

class Solution:
    def countPrimeSetBits(self, L, R):
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        count = 0
        for i in range(L, R+1):
            if bin(i)[2:].count('1') in primes:
                count += 1
        return count

class TestSolution(unittest.TestCase):
    def test_CountPrimeSetBits(self):
        pass

    def test_countPrimeSetBits(self):
        self.assertEqual(Solution().countPrimeSetBits(6, 10), 4)
        self.assertEqual(Solution().countPrimeSetBits(10, 15), 5)
        self.assertEqual(Solution().countPrimeSetBits(842, 888), 23)
        self.assertEqual(Solution().countPrimeSetBits(498484, 506588), 3117)
