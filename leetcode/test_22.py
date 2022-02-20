import unittest
from typing import *

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []
        stack.append((["("], 1, 0)) # text, # of (, # of )

        while len(stack) > 0:
            curr = stack.pop()
            if curr[1] == n:
                for _ in range(len(curr[0]), n * 2): curr[0].append(")")
                result.append("".join(curr[0]))
                continue

            if curr[1] > curr[2]:
                data = curr[0].copy()
                data.append(")")
                stack.append((data, curr[1], curr[2] + 1))

            data = curr[0]
            data.append("(")
            stack.append((data, curr[1] + 1, curr[2]))

        return result
                
            

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        data = [[1, ["()"]],
                [2, ["(())", "()()"]],
                [3, ["((()))", "(()())", "(())()", "()(())", "()()()"]],
        ]

        for a, b in data:
            self.assertEqual(s.generateParenthesis(a), b)
