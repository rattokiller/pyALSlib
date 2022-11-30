try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyalslib",
    version="1.0.0",
    description="Python implementation of the Catalog-based Aig-rewriting Approximate Logic Synthesis approximation technique",
    long_description=long_description,
    url="https://github.com/SalvatoreBarone/pyALSlib",
    author="Salvatore Barone",
    author_email="salvatore.barone@unina.it",
    classifiers=[
        "Intended Audience :: Researchers",
        "Intended Audience :: Engineers",
        "Topic :: Logic Approximation",
        "License :: GNU GPLv3",
        "Programming Language :: Python :: 3.9"
    ],
    keywords="Catalog-based Aig-rewriting Approximate Logic Synthesis approximation technique",
    packages=["pyalslib"],
    include_package_data=True,
    install_requires=["igraph", "z3-solver", "pyboolector", "python-igraph", "numpy"],
    project_urls={
        "Bug Reports": "https://github.com/SalvatoreBarone/pyALSlib/issues",
        "Source": "https://github.com/SalvatoreBarone/pyALSlib",
    },
)

