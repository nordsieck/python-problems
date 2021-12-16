import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        result = [root.val]
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result
        
class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(s.preorderTraversal(r), [1, 2, 3])

        r = None
        self.assertEqual(s.preorderTraversal(r), [])

        r = TreeNode(1)
        self.assertEqual(s.preorderTraversal(r), [1])
