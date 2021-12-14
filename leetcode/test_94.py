import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result
        
class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = None
        self.assertEqual(s.inorderTraversal(r), [])

        r = TreeNode(1, None, None)
        self.assertEqual(s.inorderTraversal(r), [1])
        
        r = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
        self.assertEqual(s.inorderTraversal(r), [1, 3, 2])
