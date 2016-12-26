from util.functions import create_dir_run_func, get_last_number
from zipfile import ZipFile
import unittest


class TestFixture(unittest.TestCase):

    RESOURCE = 'res/channel.zip'
    TARGET = '../out/05'
    README = '{}/readme.txt'.format(TARGET)

    def setUp(self):
        def extract(directory):
            with ZipFile(self.RESOURCE, 'r') as zip_ref:
                zip_ref.extractall(directory)
        create_dir_run_func(self.TARGET, func=extract)

    def test_readmeStart(self):
        with open(self.README, 'r') as f:
            text = f.read()
            num = get_last_number(text)
            self.assertEqual(90052, num)

    @unittest.skip('Skipping 06 print test to avoid cluttering CI output')
    def test_loop(self):
        next_file = 'readme'
        with ZipFile(self.RESOURCE, 'r') as zip_ref:
            text = zip_ref.open('{}.txt'.format(next_file)).read()
            num = get_last_number(text)
            result = ''
            while num:
                file_ref = '{}.txt'.format(num)
                text = zip_ref.open('{}.txt'.format(num)).read()
                info_object = zip_ref.getinfo(file_ref)
                result += info_object.comment.decode('utf-8')
                num = get_last_number(text)
        print(result)

if __name__ == '__main__':
    unittest.main()
