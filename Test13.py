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
        self.assertEqual(10**2, 10)

if __name__ == "__main__":
    #unittest.main()
    test1 = TestTest('test_one')
    test2 = TestTest('test_two')

    # test2.run()
    # test1.test_one()
    # test1.test_two()
    # result = test1.run()
    # print(result)

    test_suite = unittest.TestSuite([test2, test2])
    result = unittest.TestResult()
    test_suite.run(result)
    print(result)
    