import unittest

class Solution:
    def getImportance(self, employees, id):
        pass

class TestSolution(unittest.TestCase):
    def test_getImportance(self):
        pass

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
