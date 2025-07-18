from setuptools import setup, find_packages

setup(
    name="myutility",
    version="0.1",
    description="A simple utility package for math operations",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[],  
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
