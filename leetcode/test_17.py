import unittest
from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        ltr = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0: return []

        if len(digits) == 1: return ltr[digits[0]]
        
        if len(digits) == 2:
            for i in ltr[digits[0]]:
                for j in ltr[digits[1]]:
                    result.append(i + j)
            return result

        if len(digits) == 3:
            for i in ltr[digits[0]]:
                for j in ltr[digits[1]]:
                    for k in ltr[digits[2]]:
                        result.append(i + j + k)
            return result

        # len(digits) == 4
        for i in ltr[digits[0]]:
            for j in ltr[digits[1]]:
                for k in ltr[digits[2]]:
                    for l in ltr[digits[3]]:
                        result.append(i + j + k + l)
        return result
            

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [["23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
                ["", []],
                ["2", ["a", "b", "c"]],
                ["5678", ["jmpt","jmpu","jmpv","jmqt","jmqu","jmqv","jmrt","jmru","jmrv","jmst","jmsu","jmsv","jnpt","jnpu","jnpv","jnqt","jnqu","jnqv","jnrt","jnru","jnrv","jnst","jnsu","jnsv","jopt","jopu","jopv","joqt","joqu","joqv","jort","joru","jorv","jost","josu","josv","kmpt","kmpu","kmpv","kmqt","kmqu","kmqv","kmrt","kmru","kmrv","kmst","kmsu","kmsv","knpt","knpu","knpv","knqt","knqu","knqv","knrt","knru","knrv","knst","knsu","knsv","kopt","kopu","kopv","koqt","koqu","koqv","kort","koru","korv","kost","kosu","kosv","lmpt","lmpu","lmpv","lmqt","lmqu","lmqv","lmrt","lmru","lmrv","lmst","lmsu","lmsv","lnpt","lnpu","lnpv","lnqt","lnqu","lnqv","lnrt","lnru","lnrv","lnst","lnsu","lnsv","lopt","lopu","lopv","loqt","loqu","loqv","lort","loru","lorv","lost","losu","losv"]],
        ]

        for a, b in data:
            self.assertEqual(s.letterCombinations(a), b)
