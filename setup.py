from setuptools import setup, find_packages

setup(
    name="nandha_helper",           # Your package name
    version="0.1.0",                # Initial version
    author="Nandhagopal K",         # Your name
    author_email="nandhaxd@gmail.com",
    description="A simple helper package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nandhaxd/nandha_helper",  # Your GitHub repo
    packages=find_packages(),
    package_data={
        'nandha_helper': ['data/User-Agent.txt'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
