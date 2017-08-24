import unittest

class SumTests(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(total, int)
        self.assertEqual(total, 55)

if __name__=='__main__':
    SumTests().test_main()