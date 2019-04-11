import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

print("setup :", setuptools.find_packages())

setuptools.setup(
    name="turtle-comments-package-test-ha",
    version="0.0.1",
    author="a et h",
    author_email="alice.genestier@insa-lyon.fr",
    description="A small package to draw figures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hgit2/HPC_Docstrings",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
