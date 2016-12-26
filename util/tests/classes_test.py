from util.classes import ReportingDeque
import unittest
import re


class ReportingDequeTest(unittest.TestCase):

    def setUp(self):
        self.deque = ReportingDeque(maxlen=3)

    def test_append(self):
        self.deque.append('a')
        self.deque.append('b')
        self.deque.append('c')
        self.assertEqual(3, len(self.deque))
        self.assertEqual('a', self.deque.popleft())
        self.assertEqual('b', self.deque.popleft())
        self.assertEqual('c', self.deque.popleft())
        self.assertEqual(0, len(self.deque))

    def test_dequeAppendWhenFull(self):
        for i in range(5):
            self.deque.append(i)
        self.assertEqual(3, len(self.deque))
        self.assertEqual(2, self.deque.popleft())
        self.assertEqual(4, self.deque.pop())
        self.assertEqual(1, len(self.deque))

    def test_simpleDequeReport(self):
        for letter in 'deque':
            self.deque.append(letter)
        self.assertEqual('que', self.deque.report())

    def test_dequeReportWithCondition(self):
        for letter in 'state':
            self.deque.append(letter)
        regex = re.compile(r'^ate$')
        conditionFn = lambda x: regex.match(x)
        self.assertTrue(self.deque.report(condition=conditionFn))
        self.deque.append('!')
        self.assertFalse(self.deque.report(condition=conditionFn))

    def test_dequeReportWithCallback(self):
        for letter in 'report':
            self.deque.append(letter)
        regex = re.compile(r'^ort$')
        conditionFn = lambda x: regex.match(x)
        self.assertTrue(self.deque.report(condition=conditionFn))
        callbackFn = lambda x: x[1]
        self.assertEqual('r', self.deque.report(condition=conditionFn,
                                                callback=callbackFn))
        self.deque.append('z')
        self.assertFalse(self.deque.report(condition=conditionFn,
                                           callback=callbackFn))


if __name__ == '__main__':
    unittest.main()
