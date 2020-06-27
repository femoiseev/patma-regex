# patma-regex
A mini-library for Scale-like destructive group matching of regexes in Python using recently proposed [Structural Pattern Matching](https://www.python.org/dev/peps/pep-0622/).

# Installation
First of all, you need to install fork of alpha version of Python 3.10 that implements match / case clause ( https://github.com/brandtbucher/cpython/tree/patma):
```bash
git clone --single-branch --branch patma https://github.com/brandtbucher/cpython.git
cd cpython
./configure
make
make test
sudo make altinstall
```
The command above will install alpha-version of python 3.10 with implemented pattern matching (don't worry, it won't override your system python, just add `python3.10` into list of your python versions).

After that, you can just install this library from PyPi (I suggest you to do in into a virtualenv environment):
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install patma-regex
```

# Usage
This library allows you to use destructive matching of groups in regexes in Scala-like way. Here I provide few examples (to run them, use virtualenv environenment described in the previous section):

You can extract positional groups:
```python
from patma_regex import PatmaRegex

pattern = PatmaRegex(r"(\\w+) (\\w+)")

# The following code will print "John | Doe"
match "John Doe":
    case pattern(x, y):
        print(x + " | " + y)
```

Also, you can extract named groups:
```python
from patma_regex import PatmaRegex

pattern = PatmaRegex(r"(?P<firstname>\\w+) (?P<lastname>\\w+)")

# The following code will print "John | Doe"
match "John Doe":
    case pattern(firstname=x, lastname=y):
        print(x + " | " + y)
```

It's not necessary to refer to named groups by name, you can also do it in a positional way:
```python
from patma_regex import PatmaRegex

pattern = PatmaRegex(r"(?P<firstname>\\w+) (?P<lastname>\\w+)")

# The following code will print "John | Doe"
match "John Doe":
    case pattern(x, lastname=y):
        print(x + " | " + y)
```

Of course, you can put few `case` into `match` statement, read [PEP](https://www.python.org/dev/peps/pep-0622/) for more details.
