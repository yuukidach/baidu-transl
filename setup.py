from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name='baidu-transl',
    version='0.0.1',
    description='Python command line tool for baidu fanyi.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Dash',
    author_email='chendamailbox@foxmail.com',
    packages=find_packages(),
    install_requires= INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'bdtrans = baidu_transl.cli:run'
        ]
    }
)