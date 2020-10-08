import io 
from os.path import dirname, abspath, join
import setuptools

def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

ROOT_DIR = abspath(dirname(__file__))
PACKAGE_DIR = join(ROOT_DIR,'datacube_bigmart')
VERSION_PATH = join(PACKAGE_DIR,'version.py')

version = {}
with open(VERSION_PATH) as fp:
    exec(fp.read(), version)

setuptools.setup(name='datacube-bigmart',
                 version=version['__version__'],
                 author='Emin Mammadov',
                 author_email='emin.e.mammadov@protonmail.com',
                 url='https://github.com/iameminmammadov/BigMart',
                 packages=setuptools.find_packages(exclude=('tests',)),
                 install_requires=list_reqs(),
                 extras_require={},
                 include_package_data=True,
                 license='BSD 3',
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.6.0'
                 )

