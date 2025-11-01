from setuptools import setup, find_packages

setup(
    name="mmlabc-to-smf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mido==1.3.2",
        "tree-sitter==0.21.3",
    ],
    python_requires=">=3.8",
)
