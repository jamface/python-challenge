from setuptools import setup


setup(name='python-challenge',
      version='1.0',
      author='Jamface',
      url='https://github.com/jamface/python-challenge',
      packages=['util'],
      package_data={'', ['res/*.txt', 'res/*.zip']},
      include_package_data=True)
