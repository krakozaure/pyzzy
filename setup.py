import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyzzy",
    version="0.0.2",
    author="krakozaure",
    license="MIT",
    author_email="",
    description="Set of packages to simplify development in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krakozaure/pyzzy",
    packages=setuptools.find_packages(),
    install_requires=[
        "colorama",
        "ruamel.yaml",
        "toml",
    ],
    tests_require=[
        "pytest",
        "tox",
    ],
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ),
)