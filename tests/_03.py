from lib.classes import ReportingDeque
import unittest
import re


class TestFixture(unittest.TestCase):

    def test_scan(self):
        deque = ReportingDeque(maxlen=9)
        regex = re.compile(r'^[a-z]([A-Z]{3}[a-z]){2}$')
        conditionFn = lambda x: regex.match(x)
        callbackFn = lambda x: x[4]
        result = []
        with open('../res/equality.txt', 'r') as f:
            read_data = f.read()
            for letter in read_data:
                if letter == '\n':
                    continue
                deque.append(letter)
                match = deque.report(condition=conditionFn,
                                     callback=callbackFn)
                if match:
                    result.append(match)
        self.assertEqual('linkedlist', ''.join(result))


if __name__ == '__main__':
    unittest.main()
