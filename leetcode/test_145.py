import unittest
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        result = []
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        r = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        self.assertEqual(s.postorderTraversal(r), [3, 2, 1])

        r = None
        self.assertEqual(s.postorderTraversal(r), [])

        r = TreeNode(1)
        self.assertEqual(s.postorderTraversal(r), [1])
