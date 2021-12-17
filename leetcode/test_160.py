import unittest
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA, hA = 0, headA
        while hA is not None: lenA, hA = lenA + 1, hA.next
        
        lenB, hB = 0, headB
        while hB is not None: lenB, hB = lenB + 1, hB.next

        if lenA < lenB:
            lenA, lenB, hA, hB = lenB, lenA, headB, headA
        else:
            hA, hB = headA, headB
            
        for i in range(lenA - lenB): hA = hA.next
        while hA is not None and hB is not None:
            if hA is hB: return hA
            hA, hB = hA.next, hB.next

        return None
        
            
class TestSolution(unittest.TestCase):
    def testFn(self):
        s = Solution()

        A = ListNode(4)
        A.next = ListNode(1)
        A.next.next = ListNode(8)
        A.next.next.next = ListNode(4)
        A.next.next.next.next = ListNode(5)

        B = ListNode(5)
        B.next = ListNode(6)
        B.next.next = ListNode(1)
        B.next.next.next = A.next.next

        self.assertEqual(s.getIntersectionNode(A, B), A.next.next)

        A = ListNode(1)
        A.next = ListNode(9)
        A.next.next = ListNode(1)
        A.next.next.next = ListNode(2)
        A.next.next.next.next = ListNode(4)

        B = ListNode(3)
        B.next = A.next.next.next

        self.assertEqual(s.getIntersectionNode(A, B), A.next.next.next)
