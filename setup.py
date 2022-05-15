import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaskreactapp",
    version="0.0.1",
    author="Ilya Shnayderman",
    author_email="ilyashn@il.ibm.com",
    description="Flask and react application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilyashnil/flash-react-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 License",
        "Operating System :: OS Independent",
    ],
)