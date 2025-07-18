# test_mymath.py

import unittest
import mymath

class TestMyMath(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(mymath.add(2, 3), 5)
        self.assertEqual(mymath.add(-1, 1), 0)
        self.assertEqual(mymath.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(mymath.subtract(5, 2), 3)
        self.assertEqual(mymath.subtract(0, 4), -4)
        self.assertEqual(mymath.subtract(10, 10), 0)

if __name__ == "__main__":
    unittest.main()
