from typing import Annotated, List  # pyright: ignore[reportDeprecated]

import typer  # ignore-errors
from typer.main import Typer

from tl.utils.translation_utils import (
    get_i18n_obj,
    get_languages,
    get_languages_as_english_names,
    is_supported,
)

cli: Typer = typer.Typer(no_args_is_help=True, suggest_commands=True)


@cli.command()
def list(
    as_english: Annotated[bool, typer.Option("--english", "-e")] = False,
    use_casefold: Annotated[bool, typer.Option("--casefold", "-c")] = False,
) -> None:
    """
    List supported languages in their native or english spelling.

    Args:
        as_english (Optional[bool]): use english spelling when listing languages
        use_casefold (Optional[bool]): output results without casing

    Example:
    ```bash
    $ python -m translation_library list -l en
    $ python -m translation_library list -l de -e
    $ python -m translation_library list -l ja -c
    ```
    """
    if as_english:
        print(get_languages_as_english_names(casefold=use_casefold))
    else:
        print(get_languages(casefold=use_casefold))


@cli.command()
def translate(
    language_code: Annotated[str, typer.Option("--language", "-l")],
    key_path: Annotated[str, typer.Option("--key-path", "-k")],
    args: Annotated[List[str], typer.Argument()] = [],
) -> None:
    """
    Translate any value from a language TOML file with a specified key.

    Args:
        language_code (str): language code of the TOML file to retrieve from
        key_path (str): path to the i18n string to get in the language TOML file
        args (Optional[dict[str, object]]): optional dictionary entries to format
            into the i18n string's placeholder variables separated by spaces

    Example:
    ```bash
    $ python -m translation_library translate -l en -k confirm
    $ python -m translation_library translate -l de -k hello name=Blake
    $ python -m translation_library translate -l ja -k notifications.new_message count=1
    ```
    """
    raw_i18n_str: str = str(get_i18n_obj(language_code.lower(), key_path))

    # If "name=Blake", adds {"name": "Blake"} to placeholder_args dictionary
    if args:
        placeholder_args: dict[str, str] = {
            k: v for k, v in (arg.split("=") for arg in args)
        }
        print(raw_i18n_str.format(**placeholder_args))
    else:
        print(raw_i18n_str)


@cli.command()
def supported(
    language_code: Annotated[str, typer.Option("--language", "-l")],
) -> None:
    """
    Check if a given language is supported by your translation library.

    Args:
        language (str): the language code to check (ex: en, de, ja, etc.)

    ```bash
    $ python -m translation_library supported -l en
    $ python -m translation_library supported -l de
    $ python -m translation_library supported -l ja
    ```
    """
    print(is_supported(language_code.lower()))


@cli.command()
def i18n_print(
    language_code: Annotated[str, typer.Option("--language", "-l")],
    key_path: Annotated[str, typer.Option("--key-path", "-k")],
) -> None:
    """
    Get any value from a language TOML file with a specified key.

    Args:
        language (str): language of the i18n string(s) to print
        key_path (str): path to the i18n string(s) in the TOML file. supports globbing

    Example:
    ```bash
    $ python -m translation_library i18n-print -l de -k start.welcome
    $ python -m translation_library i18n-print -l de -k settings.*
    ```
    """
    print(get_i18n_obj(language_code.lower(), key_path))
