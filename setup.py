import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version = os.environ.get("RELEASE_VERSION", "latest")

setuptools.setup(
    name="flaskreactapp",
    version=version,
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