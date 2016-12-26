from lib.functions import get_url_resource, get_last_number, create_dir_run_func
import unittest
import shutil
import os


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


class CreateDirRunFuncTest(unittest.TestCase):

    TARGET = '../../out/test'

    def setUp(self):
        if os.path.exists(self.TARGET):
            shutil.rmtree(self.TARGET)

    def tearDown(self):
        shutil.rmtree(self.TARGET)

    def test_dirCreated(self):
        create_dir_run_func(self.TARGET)
        self.assertTrue(os.path.exists(self.TARGET))

    def test_emptyDirRunFunction(self):
        def touch(directory):
            file = '{}/test.txt'.format(directory)
            open(file, 'a').close()
        create_dir_run_func(self.TARGET, func=touch)
        self.assertTrue(os.listdir(self.TARGET))


if __name__ == '__main__':
    unittest.main()
