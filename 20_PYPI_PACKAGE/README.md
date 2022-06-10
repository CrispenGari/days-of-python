### PyPI package

In this lesson we are going to learn how we can create python packages and publish it on [PyPI](https://pypi.org/).

### Why would you want to create a package and publish it on PyPI?

A package come with a lot of advantages it allows other developers to use you package by just installing it using the following command:

```shell
pip install <package_name>
```

In this demo we are going to create a new package called `crisphello`. This package will have two functions the one that prints hello world and the other that will add numbers or strings together. We are going to have a following directory structure:

```shell
📁 root
    📁 crisphello
       - __init__.py
    - setup.py
    - README.md
```

In the `__init__.py` file we are going to have the following two functions in it:

```py
def hello(name=None):
    if name is None:
        return "Hello world!"
    else:
        return f'Hello, {name}!'

def add(num1, num2):
    return num1 + num2
```

> Note that `__init__.py` tells python that this is a package.

The `README.md` file contains the documentation on how the package can be used.

In the `setup.py` file we are going to configure our package as follows:

```py
from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A simple package'
DESCRIPTION = "This is a simple python package that is built for testing purpose."
# setting up
setup(
    name="crisphello",
    version=VERSION,
    author="Crispen Gari",
    author_email="<crispengari@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'hello', 'math'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
```

The `setup` functions takes in a lot of keyword args which are:

1. name - the name of the package which will be installed when we run pip install.
2. version - the version of the package
3. author - package author
4. author_email - package author email
5. description - this is the shorter package description.
6. long_description - this is a longer package description, normally this will be read from a file as a basic package use docummentation.
7. long_description_content_type - this tells readthedocs the Language that the long description should be transformed to.
8. install_requires - these are packages that were used during developing this package, for example `numpy`, `matplotlib` but in our case we don't have any.
9. keywords - keywords
10. classifiers - you can read more about them [here](https://pypi.org/classifiers/)

After this has been done we can build our package by running the following command:

```shell
python setup.py sdist bdist_wheel
```

### Uploading a package on `PiPY`

First you need to create a `pipy` account and have a username and password set. Then you will go to the terminal and install `twine` which helps us to upload our package on `pipy` as follows:

```shell
pip install twine
```

After installing twine then you can run the following command to upload the package to `pipy`

```shell
twine upload dist/*
```

> Make sure you are running these commands in the `root` directory of your project. After that your package will be available and users can be able to use after installing them using `pip`.

> Also note that publishing your `pypi` does not requires you to use `git` or to upload code on github.
