from setuptools import setup, find_packages

setup(
    name="string-utils",  
    version="0.1.0",  
    description="A simple Python library for string operations",
    author="Alor Arop Biong ",
    author_email="alor.arop18@gmail.com",
    url="https://github.com/alorarop/string-utils",
    packages=find_packages(),  # Automatically finds all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
