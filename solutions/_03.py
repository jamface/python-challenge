"""
You can use a deque and assess the state of it when it changes:
* xCVBzPKMn - is an example success state
* FIFO queue with a maximum of 9 elements
* Each time you recognise the success state, get the 5th element
* Combine all collected elements for the result
"""
import collections
import unittest
import re


class StateCheckDeque(collections.deque):

    def __init__(self):
        """
        Constructor
        """
        super(StateCheckDeque, self).__init__(maxlen=9)

    def report(self, condition=None, callback=None):
        """
        Report on the state of the deque.

        Args:
            condition: function that should take the state as an argument and return
                True or False if the state satisfies a given condition.
            callback: function that should be executed if the condition function
                returns True, this should take the state as an argument.
        Returns:
            String representation of the deque's state if no condition function is
            provided; True or False if a condition function is provided.
        """
        state = ''.join(self)
        if condition:
            if callback:
                return callback(state) if condition(state) else False
            else:
                return condition(state)
        return state


class TestFixture(unittest.TestCase):

    def setUp(self):
        self.deque = StateCheckDeque()

    def test_dequeAppend(self):
        self.deque.append('a')
        self.deque.append('b')
        self.deque.append('c')
        self.assertEqual(3, len(self.deque))
        self.assertEqual('a', self.deque.popleft())
        self.assertEqual('b', self.deque.popleft())
        self.assertEqual('c', self.deque.popleft())
        self.assertEqual(0, len(self.deque))

    def test_dequeAppendWhenFull(self):
        for i in range(15):
            self.deque.append(i)
        self.assertEqual(9, len(self.deque))
        self.assertEqual(6, self.deque.popleft())
        self.assertEqual(14, self.deque.pop())
        self.assertEqual(7, len(self.deque))

    def test_simpleDequeReport(self):
        for letter in 'jamsandwiches':
            self.deque.append(letter)
        self.assertEqual('andwiches', self.deque.report())

    def test_dequeReportWithCondition(self):
        for letter in 'jamsandwiches':
            self.deque.append(letter)
        regex = re.compile(r'^andwiches$')
        conditionFn = lambda x: regex.match(x)
        self.assertTrue(self.deque.report(condition=conditionFn))
        self.deque.append('!')
        self.assertFalse(self.deque.report(condition=conditionFn))

    def test_dequeReportWithCallback(self):
        for letter in 'xCMNyBAJr':
            self.deque.append(letter)
        regex = re.compile(r'^[a-z]([A-Z]{3}[a-z]){2}$')
        conditionFn = lambda x: regex.match(x)
        self.assertTrue(self.deque.report(condition=conditionFn))
        callbackFn = lambda x: x[4]
        self.assertEqual('y', self.deque.report(condition=conditionFn,
                                                callback=callbackFn))
        self.deque.append('Z')
        self.assertFalse(self.deque.report(condition=conditionFn,
                                           callback=callbackFn))

    def test_scan(self):
        regex = re.compile(r'^[a-z]([A-Z]{3}[a-z]){2}$')
        conditionFn = lambda x: regex.match(x)
        callbackFn = lambda x: x[4]
        result = []
        with open('../res/equality.txt', 'r') as f:
            read_data = f.read()
            for letter in read_data:
                if letter == '\n':
                    continue
                self.deque.append(letter)
                match = self.deque.report(condition=conditionFn,
                                          callback=callbackFn)
                if match:
                    result.append(match)
        self.assertEqual('linkedlist', ''.join(result))


if __name__ == '__main__':
    unittest.main()
