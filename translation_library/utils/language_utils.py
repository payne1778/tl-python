import logging

import tomlkit
from pydantic import Field, validate_call

from translation_library.utils.config_utils import get_language_file_path
from translation_library.utils.toml_utils import serialize_toml_dict
from translation_library.utils.translation_utils import is_supported

logger = logging.getLogger(__name__)


@validate_call
def into_toml_dict(language_code: str = Field(..., min_length=1)) -> dict[str, object]:
    """
    Returns a TOML-like dictionary with a given language code.

    Args:
        language_code (str): the code of the desired language to convert into a TOML-like dict

    Returns:
        dict: the language file as a TOML-like dict or {} if file was empty
    """
    logger.debug("language_code=%r", language_code)

    if toml_dict := serialize_toml_dict(get_language_file_path(language_code)):
        logger.info("Successfully retrieved toml dict from '%s.toml'", language_code)
        return toml_dict
    logger.warning("None dict retrieved from '%s.toml'", language_code)
    return {}


@validate_call
def into_toml_str(language_code: str = Field(..., min_length=1)) -> str:
    """
    Return the TOML language file of a given language code as a TOML-based
    pretty str.

    Args:
        language_code (str): the code of the desired language to convert into a str
    """
    logger.debug("language_code=%r", language_code)

    if not is_supported(language_code):
        logger.error("is_supported() returned False for arg: '%s'", language_code)
        raise ValueError(f"{language_code} is not supported")

    logger.debug("'%s' is supported. Converting its dictionary into str", language_code)
    if toml_str := tomlkit.dumps(into_toml_dict(language_code)):
        logger.info("Successfully converted the '%s' TOML dict into str")
        return toml_str
    logger.warning("None received from into_toml_dict() with arg '%s'", language_code)
    return ""


@validate_call
def print_toml_dict(language_code: str = Field(..., min_length=1)) -> None:
    """
    Pretty print, or print with TOML-based formatting, the language file with
    a given language code.

    Args:
        language_code (str): the code of the desired language to pretty print
    """
    logger.debug("Printing TOML file for `%s`", language_code)
    print(into_toml_str(language_code))
