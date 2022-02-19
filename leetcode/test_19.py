import unittest
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None: return False
        if self.val != other.val: return False
        if self.next is None and other.next is None: return True
        if self.next is None or other.next is None: return False
        return self.next == other.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        probe, action = head, head
        for _ in range(n): probe = probe.next

        if probe is None: return head.next
        while probe.next != None: probe, action = probe.next, action.next
        action.next = action.next.next
        return head

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()
        sol = ListNode(1, (ListNode(2, ListNode(3, ListNode(5)))))
        ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        ll = s.removeNthFromEnd(ll, 2)
        self.assertEqual(ll, sol)

        sol = None
        ll = ListNode(1)
        ll = s.removeNthFromEnd(ll, 1)
        self.assertEqual(ll, sol)

        sol = ListNode(1)
        ll = ListNode(1, ListNode(2))
        ll = s.removeNthFromEnd(ll, 1)
        self.assertEqual(ll, sol)
