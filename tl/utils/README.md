# tl-python utils

A collection of nice-to-have utility modules for the `tl-python` package.

### Interdependency Layout

| Utility Module      | Uses                                              |
| ------------------- | ------------------------------------------------- |
| `language_utils`    | `config_utils`, `toml_utils`, `translation_utils` |
| `translation_utils` | `config_utils`, `toml_utils`                      |
| `config_utils`      | `path_utils`, `toml_utils`                        |
| `toml_utils`        | `path_utils`                                      |
| `path_utils`        | —                                                 |

### Modules Information

#### > [path_utils.py](./path_utils.py)

Utilities for pathing.
Includes functions for obtaining the absolute path of the project root and checking if a path is valid.

#### > [toml_utils.py](./toml_utils.py)

Utilities for interacting with TOML files.

#### > [config_utils.py](./config_utils.py)

Utilities for interacting with the [`config.toml`](../../config.toml) file in the project root.

#### > [translation_utils.py](./translation_utils.py)

Utilities for the translation process.

#### > [language_utils.py](./language_utils.py)

Utilities for interacting with the language TOML files (files that hold the I18N strings).
