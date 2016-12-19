from urllib import request
import contextlib
import unittest

START_LINK = '12345'


def run():
    pass


class TestFixture(unittest.TestCase):

    def test_request(self):
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
        with contextlib.closing(request.urlopen(url)) as response:
            result = response.read().decode('utf-8')
            self.assertEqual('and the next nothing is 44827', result)

    


    # def _test_runner(self):
    #     # link = '12345'
    #     # link = '16044'
    #     link = '82682'
    #     # peak.html
    #     url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
    #     for i in range(400):
    #         response = request.urlopen(url.format(link))
    #         html = response.read().decode('utf-8')
    #         print(html)
    #         try:
    #             link = [int(s) for s in html.split() if s.isdigit()]
    #             if len(link) > 1:
    #                 link = link[1]
    #             else:
    #                 link = link[0]
    #         except IndexError:
    #             if html == 'Yes. Divide by two and keep going.':
    #                 link /= 2

if __name__ == '__main__':
    unittest.main()
