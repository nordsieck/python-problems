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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        if head.next is None: return head

        front, back = head, head.next
        head, front.next, back.next = back, back.next, front

        while True:
            last = front
            
            if front.next is None: return head
            if front.next.next is None: return head
            front, back = front.next, front.next.next
            last.next, front.next, back.next = back, back.next, front
            
        return head

class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        sol = None
        ll = None
        ll = s.swapPairs(ll)
        self.assertEqual(ll, sol)
        
        sol = ListNode(0)
        ll = ListNode(0)
        ll = s.swapPairs(ll)
        self.assertEqual(ll, sol)
        
        sol = ListNode(1, ListNode(0))
        ll = ListNode(0, ListNode(1))
        ll = s.swapPairs(ll)
        self.assertEqual(ll, sol)
        
        sol = ListNode(1, ListNode(0, ListNode(2)))
        ll = ListNode(0, ListNode(1, ListNode(2)))
        ll = s.swapPairs(ll)
        self.assertEqual(ll, sol)

        sol = ListNode(1, ListNode(0, ListNode(3, ListNode(2))))
        ll = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
        ll = s.swapPairs(ll)
        self.assertEqual(ll, sol)
