# simplex 0.1.1

Downloads https://pypi.python.org/pypi/simplex

Source https://github.com/numberoverzero/simplex

simple subset of regex that 'compiles' to python regexs

# Installation

`pip install simplex`

# Getting Started

```python
import simplex

pattern = "Hello, [name]"
compiled = simplex.compile(pattern)

# compiled is now a regular regexp
string = "Hello, jack and jill and world!"
match = regex.match(message)
fields = match.groupdict()
print(fields['name'])

```

# Versioning  and RFC2812

* Simplex follows semver for its **public** API.

  * Currently, `compile` is the only public function of simplex.
  * You should not rely on the internal api staying the same between minor versions.
  * Over time, private apis may be raised to become public.  The reverse will never occur.


# Contributing
Contributions welcome!  Please make sure `tox` passes (including flake8) before submitting a PR.

### Development
simplex uses `tox`, `pytest` and `flake8`.  To get everything set up:

```
# RECOMMENDED: create a virtualenv with:
#     mkvirtualenv simplex
git clone https://github.com/numberoverzero/simplex.git
pip install tox
tox
```

# API

### compile(pattern)

TODO: document the rules for compiling patterns
