import unittest
import re

class TestFixture(unittest.TestCase):

    def test_readAndReplace(self):
        with open('res/ocr.txt', 'r') as f:
            read_data = f.read()
            result = re.sub(r'[{}\[\]$%()_+!#@&^\\\n*]*', r'', read_data)
            self.assertEqual('equality', result)

if __name__ == '__main__':
    unittest.main()
