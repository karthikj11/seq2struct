import sys

from setuptools import setup, find_packages

setup(
    name='seq2struct',
    version='0.0.1',
    description='seq2struct',
    packages=find_packages(exclude=["*_test.py", "test_*.py"]),
    install_requires=[
        'asdl~=0.1.5',
        'astor~=0.7.1',
        'attrs~=18.2.0',
        'bpemb~=0.2.11',
        'cython~=0.29.1',
        'jsonnet~=0.11.2',
        'nltk~=3.4',
        'networkx~=2.2',
        'numpy~=1.15.4',
        'pyrsistent~=0.14.9',
        'stanford-corenlp~=3.9.2',
        'torch~=0.4.1' if not sys.platform.startswith('win') else 'torch @ https://download.pytorch.org/whl/cu90/torch-0.4.1-cp36-cp36m-win_amd64.whl',
        'torchtext~=0.3.1',
        'tqdm~=4.28.1',
    ],
)
