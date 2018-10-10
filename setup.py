from setuptools import setup
from poem_parser.version import __version__

setup(
    name='PoemParser',
    version=__version__,
    packages=['poem_parser',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    entry_points={
        'console_scripts': ['poem_parser=poem_parser.main:main']
    }
)
