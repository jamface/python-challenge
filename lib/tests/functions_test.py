from lib.functions import get_url_resource, get_last_number
import unittest


class GetUrlResourceTest(unittest.TestCase):

    def test_fetchAndDecode(self):
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
        result = get_url_resource(url)
        self.assertEqual('and the next nothing is 44827', result)


class GetLastNumberTest(unittest.TestCase):

    def test_noNumbers(self):
        sample = 'nothing to see here'
        self.assertEqual(None, get_last_number(sample))

    def test_oneNumber(self):
        sample = 'and the next nothing is 65432'
        self.assertEqual(65432, get_last_number(sample))

    def test_twoNumbers(self):
        sample = ('There maybe misleading numbers in the text. One example '
                  'is 82683. Look only for the next nothing and the next nothing is 63579')
        self.assertEqual(63579, get_last_number(sample))


if __name__ == '__main__':
    unittest.main()
