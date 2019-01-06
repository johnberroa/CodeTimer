import setuptools

with open("README.md", "r") as fh:  #TODO
    long_description = fh.read()

setuptools.setup(
    name='codetimer',
    version='1.0',
    scripts=['timer'],
    author="John Berroa",
    author_email="johnberroa@gmail.com",
    description="A Timer to clock any desired code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnberroa/CodeTimer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
