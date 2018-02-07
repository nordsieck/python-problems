# There is a roomba in a room that is not mapped (a grid). The roomba can turn
# pi/2 counterclockwise, it can sense if an adjacent space is traversable, or
# it can try to move one space forward. Write an algorithm to get the roomba
# to visit every position in the room that it is able to.

# All obstructions have an area (i.e. no 0 width walls).

import unittest
from enum import Enum

def neighbors(map, pos, visited):
    result = []
    for d in D:
        row = pos[0] + d.value[0]
        col = pos[1] + d.value[1]

        if row < 0 or row >= len(map): continue
        if col < 0 or col >= len(map[row]): continue
        if not map[row][col]: continue
        if (row, col) in visited: continue

        result.append((pos, d))
    return result

def traverse(map, r):
    visited = {r.pos}
    todo = []
    path = []

    todo.extend(neighbors(map, r.pos, visited))

    while len(todo) != 0:
        curr, dir = todo.pop()
        row, col = curr[0] + dir.value[0], curr[1] + dir.value[1]

        while r.pos != curr: r.move_at(map, path.pop())

        if (row, col) in visited: continue
        r.move_at(map, dir)

        visited.add(r.pos)
        path.append(rev[dir])
        todo.extend(neighbors(map, r.pos, visited))
    return visited

class D(Enum):
    _order_ = 'U L D R'
    U = (-1, 0)
    L = (0, -1)
    D = (1, 0)
    R = (0, 1)

turn = {D.U: D.L, D.L: D.D, D.D: D.R, D.R: D.U}
rev =  {D.U: D.D, D.D: D.U, D.L: D.R, D.R: D.L}

class Roomba:
    def __init__(self, pos):
        self.dir = D.U
        self.pos = pos

    def turn(self):
        self.dir = turn[self.dir]
        return self

    def face(self, dir):
        while self.dir != dir: self.turn()
        return self

    def move(self, map):
        r = self.pos[0] + self.dir.value[0]
        c = self.pos[1] + self.dir.value[1]

        if r < 0 or r >= len(map): return False
        if c < 0 or c >= len(map[r]): return False
        if map[r][c]: self.pos = (r, c)
        return map[r][c]

    def move_at(self, map, dir): return self.face(dir).move(map)

class TestSolution(unittest.TestCase):
    def test_turn(self):
        self.assertEqual(turn[D.U], D.L)
        self.assertEqual(turn[D.R], D.U)

    def test_neighbors(self):
        self.assertEqual(neighbors([[True]], (0, 0), {(0, 0)}), [])
        self.assertEqual(neighbors([[True, True, False]], (0, 1), {(0, 1)}), [((0, 1), D.L)])
        self.assertEqual(neighbors([[True, True, True]], (0, 1), {(0, 0), (0, 1)}), [((0, 1), D.R)])

    def test_traverse(self):
        self.assertEqual(traverse([[True]], Roomba((0, 0))), {(0, 0)})
        self.assertEqual(traverse([[True, True]], Roomba((0, 0))), {(0, 0), (0, 1)})
        self.assertEqual(traverse([[True, True, False]], Roomba((0, 1))), {(0, 0), (0, 1)})
        self.assertEqual(traverse([[True, True, True]], Roomba((0, 1))), {(0, 0), (0, 1), (0, 2)})

        map = [[True, False, True, True, True],
               [False, False, True, False, True],
               [True, True, True, True, True],
               [True, True, True, False, True],
               [True, True, True, False, True]]

        expected = {(0, 2), (0, 3), (0, 4),
                    (1, 2), (1, 4),
                    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                    (3, 0), (3, 1), (3, 2), (3, 4),
                    (4, 0), (4, 1), (4, 2), (4, 4)}

        self.assertEqual(traverse(map, Roomba((2, 2))), expected)

        

class TestRoomba(unittest.TestCase):
    def test_turn(self):
        r = Roomba((0, 0))
        self.assertEqual(r.turn().dir, D.L)

    def test_face(self):
        r = Roomba((0, 0))
        self.assertEqual(r.face(D.U).dir, D.U)
        self.assertEqual(r.face(D.R).dir, D.R)

    def test_move(self):
        map = [[True]]
        r = Roomba((0, 0))
        self.assertEqual(r.move(map), False)

        map = [[True, True, False]]
        r = Roomba((0, 1))
        self.assertEqual(r.face(D.R).move(map), False)
        self.assertEqual(r.face(D.L).move(map), True)
        self.assertEqual(r.pos, (0, 0))
