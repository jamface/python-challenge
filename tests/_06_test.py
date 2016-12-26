from zipfile import ZipFile
import unittest


class TestFixture(unittest.TestCase):

    def extract(self):
        with ZipFile("../res/channel.zip", "r") as zip_ref:
            zip_ref.extractall("../out/05")

    def test_stub(self):
        print('you got to this test fixture!')


if __name__ == '__main__':
    unittest.main()
