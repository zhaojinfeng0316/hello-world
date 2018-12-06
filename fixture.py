# fixture
#
import unittest
#
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")
    def test100(self):
        print("correct")
    def test200(self):
        print("error")

if __name__ == '__main__':
    unittest.main()
