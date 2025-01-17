import unittest
from src import NaivLoopUnrollingFour

class TestNaivLoopUnrollingFour(unittest.TestCase):

    def test_multiply(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
        result = NaivLoopUnrollingFour.multiply(matrix1, matrix2)
        expected_result = [[84, 90, 96], [201, 216, 231], [318, 342, 366]]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()