import unittest

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run before every test case")

    def test_methodA(self):
        print("Running Method A")

    def test_methodB(self):
        print("Running Method B")

    def tearDown(self):
        print("I will run after every test case")


if __name__ == '__main__':
    unittest.main(verbosity=2)