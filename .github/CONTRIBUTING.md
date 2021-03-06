#  Code of Conduct
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

# How to Contribute to Open Source
Want to contribute to open source?<br />
A guide to making open source contributions, for first-timers and for veterans:<br />
https://opensource.guide/

# Issues
The preferred way of giving feedback is via GitHub Issues.<br />
You should choose one of the [Issue Templates](https://github.com/djbrown/riddlebase/issues/new/choose)

# Developing Python

## Package Management
If you want to add new dependencies to the project, make sure their license is compatible with the MIT license.

This Project uses [Poetry](https://github.com/python-poetry/poetry) for managing Python Packages.<br />
Install new dependencies from pypi via `poetry add <PACKAGE>`.
Add `--dev` flag for development dependencies.

## Format and Style Guide
You can contribute to this Project using any IDE, Editor or Terminal you like, as long as your modifications obey the conventions defined by the [Style Guide for Python Code (PEP8)](https://www.python.org/dev/peps/pep-0008/).
The following command will clean your code accordingly: `poetry run autopep8 -ir .`

Also make sure to check messages from the following commands before proposing:
* `poetry run mypy .`
* `poetry run flake8`
