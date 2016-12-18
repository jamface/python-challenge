import unittest

class TestFixture(unittest.TestCase):

    def test_solution(self):
        self.assertEqual('274877906944', str(2 ** 38))

if __name__ == '__main__':
    unittest.main()
