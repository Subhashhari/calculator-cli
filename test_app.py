import unittest
from app import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', 5, 5), 10)

    def test_sub(self):
        self.assertEqual(calculate('sub', 10, 5), 5)
        
    def test_mul(self):
        self.assertEqual(calculate('mul', 3, 3), 9)

if __name__ == '__main__':
    unittest.main()