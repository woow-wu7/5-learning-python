import unittest

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        print('2+2=4')
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        print('5-3=2')
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()