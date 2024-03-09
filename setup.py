#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["bibtexparser>=1.4.1","levenshtein>=0.25.0"]

test_requirements = [
    "pytest>=3",
]


setup(
    author="C Sh",
    author_email="NONE@gmail.com",
    python_requires=">=3.11",

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    description="bibtex format",
    entry_points={
        "console_scripts": [
            "bibformat=bibformat:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="bibformat",
    name="bibformat",
    packages=find_packages(include=["bibformat", "bibformat.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/cshen/bibformat",
    version="1.0.0",
    zip_safe=False,
)

