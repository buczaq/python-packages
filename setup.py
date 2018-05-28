from setuptools import setup, find_packages

setup(
    name='hmcalc',
    version='0.5.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='calculation packages',
    long_description=open('README.md').read(),
    url='https://github.com/buczaq/python-packages',
    author='Krzysztof Buczak',
    author_email='226153@student.pwr.edu.pl'
)
