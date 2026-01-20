import logging

from pydantic import Field, validate_call

from translation_library.utils.config_utils import (
    get_all_english_names,
    get_all_language_codes,
    get_all_native_names,
    get_language_file_path,
)
from translation_library.utils.toml_utils import get_value_from_key

logger = logging.getLogger(__name__)


def get_languages(casefold: bool = False) -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its native spelling:

    >>> ["English", "Deutsch", "日本語"]

    Or with casefold:

    >>> ["english", "deutsch", "日本語"]

    Args:
        casefold (Optional[bool]): use caseless strs if true, otherwise use default casing

    Returns:
        list[str]: list of all supported languages with their native spelling
    """
    languages: list[str]
    logger.debug("'casefold'=%r", casefold)
    if casefold:
        languages = [name.casefold() for name in get_all_native_names()]
    else:
        languages = get_all_native_names()
    logger.info("Languages: %r", languages)
    return languages


def get_languages_as_english_names(casefold: bool = False) -> list[str]:
    """
    Returns a list of all supported languages according to the languages TOML
    file. Each entry in the list is the language spelled in its english
    spelling:

    >>> ["English", "German", "Japanese"]

    Or with casefold:

    >>> ["english", "german", "japanese"]

    Args:
        casefold (Optional[bool]): use caseless strs if true, otherwise use default casing

    Returns:
        list[str]: list of all supported languages with their english spelling
    """
    languages: list[str]
    logger.debug("'casefold'=%r", casefold)
    if casefold:
        languages = [name.casefold() for name in get_all_english_names()]
    else:
        languages = get_all_english_names()
    logger.info("Languages: %r", languages)
    return languages


@validate_call
def is_supported(language_code: str = Field(..., min_length=1)) -> bool:
    """
    Checks to see if a given language is supported.

    Args:
        language_code (str): the language code to check if supported

    Returns:
        bool: `True` if the language is supported, `False` otherwise
    """
    logger.debug("'language_code'=%r", language_code)
    supported: bool = language_code in get_all_language_codes()
    logger.debug("'%s' is supported? '%s'", language_code, str(supported))
    return supported


@validate_call
def get_i18n_obj(
    language_code: str = Field(..., min_length=1),
    key_path: str = Field(..., min_length=1),
) -> object:
    """
    Get the value of a specific key from a given language TOML file.

    Args:
        language_code (str): the language's code from which to retrieve the i18n object
        key_path (str): the key's path in the specified language TOML file. supports globbing.

    Returns:
        object: the value (as an object) of associated with the given key
    """
    if not is_supported(language_code):
        logger.error("is_supported() returned 'False' for arg: '%s'", language_code)
        raise ValueError(f"{language_code} is not supported")

    logger.debug(
        "'%s' is supported. Getting value with '%s' from TOML file"
        % (language_code, key_path)
    )
    if value := get_value_from_key(get_language_file_path(language_code), key_path):
        logger.info(
            "Successfully retrieved '%s' with key '%s' from '%s' TOML file",
            value,
            key_path,
            language_code,
        )
        return value
    logger.warning(
        "None value retrieved with key '%s' from '%s' TOML file",
        key_path,
        language_code,
    )
    return None
