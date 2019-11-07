
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toSpcy", # Replace with your own username
    version="1.0.0",
    author="Patrick Ruan",
    author_email="acdmc.wruan@gmail.com",
    description="This package aims to initialize training data for SpaCy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrick013",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)