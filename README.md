# Advent of Code 2025

Python solutions to the Advent of Code 2025.

Requires Python 3.13.

## Usage

Using my [aoc-runner](https://github.com/OverkillGuy/aoc-runner) to run these
solution as plugins:

Ensure you have aoc-runner installed in your current venv first.
Once that's done, check your plugins are available:

``` shell
aoc discover  # Should find your plugins!
```

Then you can play the solution against your input:

``` shell
aoc run 2025-2-1 data/input02.txt
```

## Development

### Python setup

This repository uses Python3.13, using
[uv](https://docs.astral.sh/uv/) as package manager to define a
Python package inside `src/aoc2025/`.

`uv` will create virtual environments if needed, fetch
dependencies, and install them for development.

For ease of development, a `Makefile` is provided, use it like this:

```shell
make  # equivalent to "make all" = install lint docs test build
# run only specific tasks:
make install
make lint
make test
# Combine tasks:
make install test
```

Once installed, the module's code can now be reached through running
Python in uv:

```shell
$ uv run python
>>> from aoc2025 import day1
>>> day1.solution1("R100")
```

This codebase uses [pre-commit](https://pre-commit.com) to run linting
tools like `ruff`. Use `pre-commit install` to install git
pre-commit hooks to force running these checks before any code can be
committed, use `make lint` to run these manually. Testing is provided
by `pytest` separately in `make test`.

### Documentation

Documentation is generated via [Sphinx](https://www.sphinx-doc.org/en/master/),
using the cool [myst_parser](https://myst-parser.readthedocs.io/en/latest/)
plugin to support Markdown files like this one.

Other Sphinx plugins provide extra documentation features, like the recent
[sphinx-autodoc2](https://sphinx-autodoc2.readthedocs.io/en/latest/index.html)
to generate API reference without headaches, and with myst-markdown support in
docstrings too!

To build the documentation, run

```shell
# Requires the project dependencies provided by "make install"
make docs
# Generates docs/build/html/
```

To browse the web version of the documentation you just built, run:

```shell
make docs-serve
```

And remember that `make` supports multiple targets, so you can generate the
documentation and serve it:

```shell
make docs docs-serve
```

### Templated repository

This repository was created by the copier template available at
/home/jiby/dev/ws/python-template, using version v2.0.0a24.
