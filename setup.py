from setuptools import setup, find_packages

setup(
    name='baidu-transl',
    version='0.0.1',
    description='Python command line tool for baidu fanyi.',
    author='Dash',
    author_email='chendamailbox@foxmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bdtrans = baidu_transl.cli:run'
        ]
    }
)