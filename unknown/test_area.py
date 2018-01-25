# You are given an array of integers that represent heights. Areas are calculated by taking the width of a
# rectangle and multiplying it by the minimum of each of the heights in the rectangle. Find the largest
# rectangle give the array.

# example: largest rect = 16

#   |-|
#   | |
#   | |       |-|
#   | | |-|   | |
#   | |-| |   | |
#   |x|x|x|x| | |
# |-|x|x|x|x| | |
# | |x|x|x|x|-| |
# | |x|x|x|x| | |-|
# -----------------
#  3 9 5 6 4 2 7 1

import unittest

def largest(data):
    largest = 0
    stack = [(-1, -1)]

    for idx, val in enumerate(data):
        if stack[-1][1] < val:
            stack.append((idx, val))
        elif stack[-1][1] > val:
            curr = None

            while stack[-1][1] > val:
                curr = stack.pop()
                if (idx - curr[0]) * curr[1] > largest: largest = (idx - curr[0]) * curr[1]

            stack.append((curr[0], val))

    while len(stack) > 1:
        curr = stack.pop()
        if (len(data) - curr[0]) * curr[1] > largest: largest = (len(data) - curr[0]) * curr[1]

    return largest
            
            

class TestSolution(unittest.TestCase):
    d = [
        [1],
        [1, 2],
        [2, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 9, 5, 6, 4, 2, 7, 1],
    ]

    def test_largest(self):
        self.assertEqual(largest(self.d[0]), 1)
        self.assertEqual(largest(self.d[1]), 2)
        self.assertEqual(largest(self.d[2]), 2)
        self.assertEqual(largest(self.d[3]), 9)
        self.assertEqual(largest(self.d[4]), 9)
        self.assertEqual(largest(self.d[5]), 16)
