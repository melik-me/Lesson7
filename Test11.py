import unittest

def func():
    return 100

class TestTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_one(self):
        #TODO something
        self.assertEqual(func(), 100)

    def test_two(self):
        self.assertEqual(10**2, 100)

if __name__ == "__main__":
    unittest.main()