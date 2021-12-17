import unittest
from typing import *

class MinStack:

    def __init__(self):
        self.data = []
        
    def push(self, val: int) -> None:
        if len(self.data) == 0: self.data.append((val, val))
        elif val < self.data[-1][1]: self.data.append((val, val))
        else: self.data.append((val, self.data[-1][1]))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

    def raw(self):
        return self.data


class TestSolution(unittest.TestCase):
    def testFn(self):
        m = MinStack()
        m.push(1)
        self.assertEqual(m.raw(), [(1, 1)])
        
        m.push(2)
        self.assertEqual(m.raw(), [(1, 1), (2, 1)])
        
        m.push(0)
        self.assertEqual(m.raw(), [(1, 1), (2, 1), (0, 0)])

        m.pop()
        self.assertEqual(m.raw(), [(1, 1), (2, 1)])
        
        m = MinStack()
        m.push(-2)
        m.push(0)
        m.push(-3)
        self.assertEqual(m.getMin(), -3)
        m.pop()
        self.assertEqual(m.top(), 0)
        self.assertEqual(m.getMin(), -2)
