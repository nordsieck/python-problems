import unittest

class Solution:
    def getImportance(self, employees, id):
        dir, todo, sum = {}, [id], 0
        for employee in employees: dir[employee.id] = employee
        
        while len(todo) != 0:
            curr = dir[todo.pop()]
            sum += curr.importance
            for s in curr.subordinates:
                todo.append(s)

        return sum
            

class TestSolution(unittest.TestCase):
    def test_getImportance(self):
        self.assertEqual(Solution().getImportance([Employee(3, 7, [])], 3), 7)
        self.assertEqual(Solution().getImportance([Employee(3, 7, []), Employee(4, 2, [])], 3), 7)
        self.assertEqual(Solution().getImportance([Employee(3, 7, [4]), Employee(4, 2, [])], 3), 9)

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
