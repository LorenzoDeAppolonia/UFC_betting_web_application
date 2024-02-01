import setuptools
from setuptools import setup

setup(name='ufc_betting',
      version='1.2.3',
      author='Honcharov, De Appolonia',
      author_email='lorenzoacg@gmail.com',
      description='Library for betting on UFC fights and getting fights and fighters statistics',
      package_dir={'': '.'},
      packages=setuptools.find_packages(where='.'),
      python_requires='>=3.11',
      )
