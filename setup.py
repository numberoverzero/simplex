""" Setup file """
import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.markdown')).read()

REQUIREMENTS = [
]

TEST_REQUIREMENTS = [
    'tox',
    'pytest',
    'pytest-cov',
    'coverage',
    'flake8'
]

if __name__ == "__main__":
    setup(
        name='simplex',
        version='0.1.2',
        description="simple subset of regex",
        long_description=README,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Software Development :: Libraries',
        ],
        author='Joe Cross',
        author_email='joe.mcross@gmail.com',
        url='https://github.com/numberoverzero/simplex',
        license='MIT',
        keywords='re regex regexp',
        platforms='any',
        include_package_data=True,
        py_modules=['simplex'],
        install_requires=REQUIREMENTS,
        tests_require=REQUIREMENTS + TEST_REQUIREMENTS,
    )
