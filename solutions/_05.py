import unittest
import pickle
from urllib import request


class TestFixture(unittest.TestCase):

    def test_pickle(self):
        response = request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
        result = response.read()
        for line in pickle.loads(result):
            for tuple in line:
                for i in range(tuple[1]):
                    print(tuple[0], end='', flush=True)
            print()


if __name__ == '__main__':
    unittest.main()
