# Translation-Library-Python

### TL-PYTHON OPERATIONAL STATUS: _Working!_

> [!NOTE]
> I am currently working on a massive overhaul with the TL Python implementation.
> Conversion to an official Python package, reconstruction the CLI, and implementation with feature-rich libraries are underway.
> For right now, this package is expected to be a little unstable.

### Overhaul Progress:

- Converted source code into a local package
- Added a `utils` for handy utilities for pathing and interacting with TOML files
- Added test cases for functions within the pathing, TOML, and language utilities
- Added `Pydantic` validation for function args
- Add a logging system
- Add docstring documentation to functions existing
- Use a library to handle sysargs in the CLI
- Add a nice way to format placeholder args for the new CLI (in stark contrast to the old hand-made CLI)

### Future Project Goals:

- Make source code a public package available on PIP
- Start using semantic versioning after soon (might be after 1.0.0 😭)
- Implement, test, and document utility functions for interaction with `config.toml`

### Suggestions & Improvements

If you have any suggestions and ideas for improvement with this project, feel free to reach out and/or [leave an issue in this repo](https://github.com/payne1778/Translation-Library-Python/issues) or [the parent mono repo](https://github.com/payne1778/Translation-Library)!
