from zipfile import ZipFile
import unittest
import os


def extract():
    with ZipFile("../res/channel.zip", "r") as zip_ref:
        zip_ref.extractall("../out/05")


class TestFixture(unittest.TestCase):

    def setUp(self):
        if not os.listdir('../out/05'):
            extract()

    def test_filesExtracted(self):
        self.assertTrue(os.listdir('../out/05'))

    def test_stub(self):
        pass



if __name__ == '__main__':
    unittest.main()