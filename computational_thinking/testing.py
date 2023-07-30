import unittest


def suma(num_1, num_2):
    return num_1 + num_2

class SumaTest(unittest.TestCase):

    def test_sum_two_positive_numbers(self):
        num_1 = 10
        num_2 = 7
        result = suma(num_1, num_2) 
        self.assertEqual(result, 17)

    def test_sum_two_negative_numbers(self):
        num_1 = -5
        num_2 = -3
        result = suma(num_1, num_2) 
        self.assertEqual(result, -8)
        

if __name__ == "__main__":
    unittest.main()
