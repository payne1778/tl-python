# mypy: ignore-errors

import logging
from pathlib import Path

from tl.utils.path_utils import get_project_root
from tl.utils.toml_utils import get_value_from_key

logger = logging.getLogger(__name__)


def get_config_file_path() -> Path:
    return get_project_root() / "config.toml"


def get_value_from_config(
    key_path: str,
) -> str | list[str] | list[dict[str, object]]:
    """
    Get a specified value from the config file.

    Args:
        key_path (str): path of the key whose value to retrieve

    Returns:
        str | list[str] | list[dict[str, object]]: the value from the config file
    """
    return get_value_from_key(get_config_file_path(), key_path)


def get_i18n_dir_path() -> Path:
    """
    Get the path of the i18n directory, which should be stored in the config file.

    Returns:
        Path: i18n_dir path if in the config file, or current directory (".")
    """
    return Path(str(get_value_from_config("paths.i18n_dir")))


def get_fallback_language_code() -> str:
    """
    Get the language code of the fallback language. Used if a given preferred
    language is not supported or not available for usage. If the fallback
    language is unspecified or otherwise unavailable, this function will
    return an empty string.

    Returns:
        str: the fallback language code, or an empty str if unavailable
    """
    return str(get_value_from_config("languages.fallback"))


def get_all_english_names() -> list[str]:
    """
    Gets a list of all supported languages with their english spelling. If the
    english spelling for each language is unspecified or otherwise unavailable,
    this function will return an empty list.

    Returns:
        list[str]: a list of all supported languages with english spelling
    """
    return [str(name) for name in get_value_from_config("languages.*.english_name")]


def get_all_native_names() -> list[str]:
    """
    Gets a list of all supported languages with their native spelling. If the
    native spelling for each language is unspecified or otherwise unavailable,
    this function will return an empty list.

    Returns:
        list[str]: a list of all supported languages with native spelling
    """
    return [str(name) for name in get_value_from_config("languages.*.native_name")]


def get_all_file_names() -> list[str]:
    """
    Get a list of all support language's file names. This list does not represent
    the language file's absolute/relative paths, just the individual file names.
    If the file names for each language is unspecified or otherwise unavailable,
    this function will return an empty list.

    Returns:
        list[str]: a list of the filenames for all supported languages
    """
    return [str(name) for name in get_value_from_config("languages.*.file")]


def get_all_language_codes() -> list[str]:
    """
    Get a list of all language codes for the supported languages. If the
    language codes for each language is unspecified or otherwise unavailable,
    this function will return an empty list.

    Returns:
        list[str]: a list of language codes for each supported language
    """
    return [code for code in get_value_from_config("languages").keys()]


def language_code_to_english_name(code: str) -> str:
    """
    Convert a language code into the language name with english spelling. If the
    english spelling is unspecified or otherwise unavailable, this function will
    return an empty string.

    Args:
        code (str): the language code to convert (case sensitive)

    Raises:
        KeyError: if the given language code does not exist in the config file

    Returns:
        str: the language name in english, or empty str if english is unavailable
    """
    return str(get_value_from_config(f"languages.{code.lower()}.english_name"))


def language_code_to_native_name(code: str) -> str:
    """
    Convert a language code into the language name with native spelling. If the
    native spelling is unspecified or otherwise unavailable, this function will
    return an empty string.

    Args:
        code (str): the language code to convert (case sensitive)

    Raises:
        KeyError: if the given language code does not exist in the config file

    Returns:
        str: the language name in native spelling, or empty str if spelling is unavailable
    """
    return str(get_value_from_config(f"languages.{code.lower()}.native_name"))


def language_code_to_file_name(code: str) -> str:
    """
    Convert a language code into the language file name. If the file name is
    unspecified or otherwise unavailable, this function will return an empty string.

    Args:
        code (str): the language code to convert (case sensitive)

    Raises:
        KeyError: if the given language code does not exist in the config file

    Returns:
        str: the language name in native spelling, or empty str if spelling is unavailable
    """
    return str(get_value_from_config(f"languages.{code.lower()}.file"))


def get_language_file_path(code: str) -> Path:
    """
    Get the absolute path of a specified language TOML file.

    Args:
        code (str): the language code whose language file path to get (case sensitive)

    Raises:
        KeyError: if the given language code does not exist in the config file

    Returns:
        Path: the absolute path of the specified language file
    """
    return get_i18n_dir_path() / language_code_to_file_name(code)
