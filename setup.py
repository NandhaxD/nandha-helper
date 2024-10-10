from setuptools import setup, find_packages

setup(
    name='nandha_helper',  # Replace with your actual package name
    version='0.1.0',
    packages=find_packages(),
    description='A simple package with one class',
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    author='Nandhagopal K',
    author_email='nandhaxd@gmail.com',
    url='https://github.com/nandhaxd/nandha_helper',  # Replace with your project URL
    license='MIT',
    install_requires=[],  # List any dependencies your package needs
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)  
