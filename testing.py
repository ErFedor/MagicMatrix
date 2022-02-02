import unittest
from matrix_gen1 import matrix

# (N*(N^2+1))/2
class Test(unittest.TestCase):
    def setUp(self):
        self.mat = matrix()
    def test_3(self):
        self.assertEqual(self.mat.Sum(3), int((3*(3**2+1))/2))
    def test_4(self):
        self.assertEqual(self.mat.Sum(4), int((4*(4**2+1))/2))
    def test_5(self):
        self.assertEqual(self.mat.Sum(5), int((5*(5**2+1))/2))
    def test_10(self):
        self.assertEqual(self.mat.Sum(8), int((8*(8**2+1))/2))
    def test_15(self):
        self.assertEqual(self.mat.Sum(15), int((15*(15**2+1))/2))


if __name__ == "__main__":
    unittest.main()