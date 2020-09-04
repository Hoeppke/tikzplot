import setuptools


with open('README.md', 'r') as fstream:
    long_description = fstream.read()

setuptools.setup(
    name="tikzplot-choeppke", # Replace with your own username
    version="0.0.1",
    author="Christoph Hoeppke",
    author_email="christoph.hoeppke@gmail.com",
    description="A python package for simple tikz based plots.",
    long_description=long_description,
    long_description_content_type="python/latex",
    url="https://github.com/Hoeppke/tikzplot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
