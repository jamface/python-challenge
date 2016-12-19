from urllib import request
import contextlib
import unittest


def run():
    """
    The run loop.
    """
    link = '12345'
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
    for i in range(400):
        response = request.urlopen(url.format(link))
        html = response.read().decode('utf-8')
        if html == 'peak.html':
            return True
        try:
            link = extractLink(html)
        except IndexError:
            if html == 'Yes. Divide by two and keep going.':
                link /= 2


def extractLink(response):
    """
    Extracts the numerical link from the response text.
    """
    numberList = [int(s) for s in response.split() if s.isdigit()]
    return numberList[0] if len(numberList) == 1 else numberList[1]


class TestFixture(unittest.TestCase):

    def test_request(self):
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
        with contextlib.closing(request.urlopen(url)) as response:
            result = response.read().decode('utf-8')
            self.assertEqual('and the next nothing is 44827', result)

    def test_extractLink(self):
        responseOne = 'and the next nothing is 65432'
        responseTwo = 'and the next nothing is 954'
        self.assertEqual(65432, extractLink(responseOne))
        self.assertEqual(954, extractLink(responseTwo))

    def test_extractLinkTwoNumbers(self):
        response = ('There maybe misleading numbers in the text. One example '
                    'is 82683. Look only for the next nothing and the next nothing is 63579')
        self.assertEqual(63579, extractLink(response))

    def test_run(self):
        self.assertTrue(run())


if __name__ == '__main__':
    unittest.main()
