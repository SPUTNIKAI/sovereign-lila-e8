from setuptools import setup, find_packages

setup(
    name="sovereign-lila-e8",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.0",
        "sentencepiece",
        "datasets",
        "requests",
    ],
)
