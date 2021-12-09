import unittest
import array

class Heap:
    def __init__(self, dtype = "i", data = [], lessThan = True):
        self.data = array.array("i", data)
        if lessThan:
            self.fn = lambda a, b: a < b
        else:
            self.fn = lambda a, b: a > b

    def raw(self):
        return self.data

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.append(e)
        n = len(self.data) - 1
        p = int((n + 1) / 2 - 1)

        while (p >= 0) and (self.fn(self.data[n], self.data[p])):
            self.data[n], self.data[p] = self.data[p], self.data[n]
            n, p = p, int((p + 1) / 2 - 1)

    def pop(self):
        if self.__len__() == 0: return None

        ret = self.data[0]
        val = self.data.pop()
        if self.__len__() > 0: self.data[0] = val

        n = 0
        while self.__len__() > n * 2 + 2:
            child = n * 2 + 1
            if self.fn(self.data[child + 1], self.data[child]):
                if not self.fn(self.data[child + 1], self.data[n]): break

                self.data[n], self.data[child + 1] = self.data[child + 1], self.data[n]
                n = chlid + 1
            else:
                if not self.fn(self.data[child], self.data[n]): break

                self.data[n], self.data[child] = self.data[child], self.data[n]
                n = child

        child = n * 2 + 1
        if self.__len__() == child + 1 and self.fn(self.data[child], self.data[n]):
            self.data[n], self.data[child] = self.data[child], self.data[n]

        return ret

class TestHeap(unittest.TestCase):
    def test_heap_len(self):
        h = Heap()
        self.assertEqual(len(h), 0)

        h = Heap(data = [0])
        self.assertEqual(len(h), 1)

    def test_heap_raw(self):
        h = Heap()
        self.assertEqual(h.raw(), array.array("i", []))

        h = Heap(data = [1, 2, 3])
        self.assertEqual(h.raw(), array.array("i", [1, 2, 3]))

    def test_heap_push(self):
        h = Heap()
        h.push(1)
        self.assertEqual(h.raw(), array.array("i", [1]))

        h.push(2)
        self.assertEqual(h.raw(), array.array("i", [1, 2]))

        h.push(3)
        h.push(4)
        h.push(5)
        self.assertEqual(h.raw(), array.array("i", [1, 2, 3, 4, 5]))

        # max
        h = Heap(lessThan = False)
        for i in range(5):
            h.push(i)
        self.assertEqual(h.raw(), array.array("i", [4, 3, 1, 0, 2]))

    def test_heap_pop(self):
        h = Heap()
        v = h.pop()
        self.assertEqual(len(h), 0)
        self.assertEqual(v, None)

        h.push(1)
        v = h.pop()
        self.assertEqual(len(h), 0)
        self.assertEqual(v, 1)

        h = Heap(data = [1, 2, 5, 3, 4, 6, 7])
        v = h.pop()
        self.assertEqual(v, 1)
        self.assertEqual(h.raw(), array.array("i", [2, 3, 5, 7, 4, 6]))

        h = Heap(lessThan = False)
        for i in range(5):
            h.push(i)
        self.assertEqual(h.raw(), array.array("i", [4, 3, 1, 0, 2]))
        val = h.pop()
        self.assertEqual(val, 4)
        self.assertEqual(h.raw(), array.array("i", [3, 2, 1, 0]))
