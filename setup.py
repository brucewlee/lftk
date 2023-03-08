from distutils.core import setup
from setuptools import find_packages
# python setup.py sdist
# python -m twine upload dist/*
setup(
    name = 'lftk',  
    version='1.0.2',
    license='CC BY-NC 4.0',   
    description = 'Comprehensive Multilingual Linguistic Features Extraction in Python',
    author = 'Bruce W. Lee',
    author_email = 'brucelws@seas.upenn.edu', 
    packages=find_packages(),
    url='https://github.com/brucewlee/lftk',
    keywords='linguistic feature',
    install_requires=[
          'pandas',
          'ndjson',
          'spacy'
      ],
    include_package_data=True,
    package_data={'': ['resources/*']}
)