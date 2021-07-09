from setuptools import setup


setup(
  name='cnfcli',
  version='1.0.1',
  description='A CLI tool for command-not-found.com',
  url='https://github.com/casparwylie/cnfcli',
  author='Caspar Wylie',
  author_email='casparwylie@gmail.com',
  entry_points={'console_scripts': ['cnf=src.cnf:main']},
  packages=['src'],
  install_requires=['bs4', 'requests'],
  python_requires='>=3.8')
