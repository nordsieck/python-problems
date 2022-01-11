import unittest
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # head
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        
        # body
        curr = head
        if curr is None: return None
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        input = (ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6)
        output = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        self.assertEqual(s.removeElements(input[0], input[1]), output)

        input = (None, 1)
        output = None
        self.assertEqual(s.removeElements(input[0], input[1]), output)

        input = (ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7)
        output = None
        self.assertEqual(s.removeElements(input[0], input[1]), output)
