from setuptools import setup


setup(name='python-challenge',
      version='1.0',
      author='Jamface',
      url='https://github.com/jamface/python-challenge',
      packages=['util'],
      data_files=[('res', ['res/equality.txt',
                           'res/ocr.txt',
                           'res/*.zip'])])
