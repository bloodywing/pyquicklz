import os
from setuptools import find_packages, setup

try:
    from pypandoc import convert_file
    read_md = lambda f: convert_file(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requirements = [
    "cffi>=1.0.0"
]

setup(
    name='pyquicklz',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    install_requires=requirements,
    cffi_modules=["quicklz/build_extension.py:ffibuilder"],
    include_dirs=['.'],
    description='Deviantart API (OAuth2) for your django project',
    long_description=read_md('README.md'),
    url='https://github.com/bloodywing/pyqicklz',
    author='Pierre Geier',
    author_email='pierre@isartistic.biz',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
