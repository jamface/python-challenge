from util.functions import get_url_resource
import unittest
import pickle


class TestFixture(unittest.TestCase):

    def test_pickle(self):
        result = get_url_resource('http://www.pythonchallenge.com/pc/def/banner.p', decoding=None)
        for line in pickle.loads(result):
            for tup in line:
                for i in range(tup[1]):
                    print(tup[0], end='', flush=True)
            print()


if __name__ == '__main__':
    unittest.main()
