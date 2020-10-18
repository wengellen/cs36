import unittest
import random
from single_number import single_number, single_number_pointers,   single_number_pointers_sorted

class Test(unittest.TestCase):
    def test_single_number(self):
        arr = []

        for i in range(10000):
            arr.append(i)
            arr.append(i)
        random.shuffle(arr)
        arr.sort()
        rand_index = random.randint(0, len(arr))
        num = arr.pop(rand_index)


        self.assertEqual(single_number(arr), num)

    def test_single_number_pointers(self):
        arr = []
        for i in range(10000):
            arr.append(i)
            arr.append(i)

        random.shuffle(arr)
        arr.sort()
        rand_index = random.randint(0, len(arr))
        num = arr.pop(rand_index)

        self.assertEqual(single_number_pointers(arr), num)


if __name__ == '__main__':
    unittest.main()