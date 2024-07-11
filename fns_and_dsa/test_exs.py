import unittest

def squre (x):
    return x*x


class testsqure(unittest.TestCase):
    def test_squre(self):
        result = squre(3)
        self.assertEqual(result,9)

if __name__ == "__main__":
    unittest.main()

