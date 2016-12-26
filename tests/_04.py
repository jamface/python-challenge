from lib.functions import get_url_resource, get_last_number
import unittest


def run():
    """
    The run loop.
    """
    link = '12345'
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
    for i in range(400):
        html = get_url_resource(url.format(link))
        if html == 'peak.html':
            return True
        try:
            link = get_last_number(html)
        except IndexError:
            if html == 'Yes. Divide by two and keep going.':
                link /= 2


class TestFixture(unittest.TestCase):

    def test_run(self):
        self.assertTrue(run())


if __name__ == '__main__':
    unittest.main()
