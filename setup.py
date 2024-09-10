# setup.py
from setuptools import setup, find_packages

setup(
    name="my_bond_package",
    version="0.1.0",
    author="bin",
    author_email="your_email@example.com",
    description="A Python package for bond price, YTM, duration, and convexity calculations.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_bond_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[],
)
