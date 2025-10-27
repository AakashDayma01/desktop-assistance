import unittest
import desctop_assis as da

class TestDesctopAssis(unittest.TestCase):

    def test_add(self):
        self.assertEqual(da.add(2, 3), 5)
        self.assertEqual(da.add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(da.multiply(2, 3), 6)
        self.assertEqual(da.multiply(-1, 5), -5)      

    def test_divide(self):
        self.assertAlmostEqual(da.divide(2, 3), 2/3)
        self.assertAlmostEqual(da.divide(-1, 5), -0.2)
    
    def test_subtract(self):
        self.assertEqual(da.subtract(3, 2), 1)
        self.assertEqual(da.subtract(-2, 1), -3)

if __name__ == "__main__":
    unittest.main()
