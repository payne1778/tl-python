import logging
from pathlib import Path
from typing import Annotated

import tomlkit
from glom import glom  # type: ignore
from glom.core import PathAccessError  # type: ignore
from pydantic import BeforeValidator, Field, validate_call
from tomlkit.exceptions import EmptyKeyError, EmptyTableNameError

from translation_library.utils.path_utils import valid_path_validator

logger = logging.getLogger(__name__)


def valid_toml_path_validator(v: str | Path) -> Path:
    """
    Checks to see if a given path has the `.toml` extension. If so, it will
    call the valid_path_validator from the path_utils module to see if it exists.

    Args:
        v (str | Path): a supposed `str`/`Path` path to a TOML file

    Raises:
        ValueError: if a `str`/`Path` was given and it does not end in ".toml"

    Returns:
        Path: the original path if it exists, otherwise, valid_path_validator() will raise errors
    """
    logger.debug("'path'=%r", v)
    if isinstance(v, str) and not v.endswith(".toml"):
        logger.error("arg '%s' did not end in .toml", v)
        raise ValueError("TOML file path must end in .toml")

    if isinstance(v, Path) and v.suffix != ".toml":
        logger.error("arg '%s' did not end in .toml", v)
        raise ValueError("TOML file path must end in .toml")

    logger.debug("Path is TOML file, now checking existence: %r", v)
    return valid_path_validator(v)


@validate_call
def serialize_toml_dict(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
) -> dict[str, object]:
    """
    Return a TOML file as a dictionary of key-value pairs from a specified
    directory path.

    Args:
        toml_file_path (str | Path): the path of the TOML file to be loaded

    Raises:
        RuntimeError: if an unknown/unchecked exception occurs when opening file

    Returns:
        dict: the TOML-like dict obtained from the given TOML language file pah
    """
    try:
        with open(toml_file_path, "rb") as f:
            if toml_data := tomlkit.load(f):
                logger.debug("TOML successfully serialized from '%s'", toml_file_path)
                return toml_data
            logger.warning("None value serialized from '%s", toml_file_path)
            return {}
    except (EmptyKeyError, EmptyTableNameError) as ee:
        logger.exception("TOML file '%s' has invalid syntax", toml_file_path)
        raise ee
    except Exception as e:
        logger.exception("Could not serialize '%s' due to: ", toml_file_path)
        raise e


@validate_call
def deserialize_toml_dict(
    toml_data: Annotated[dict[str, object], Field(..., min_length=1)],
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
) -> None:
    """
    Write a TOML-like dictionary to an specified, pre-existing TOML file path.

    Args:
        toml_file_path (str | Path): TOML-like dictionary to be deserialized
        toml_data (dict): path of the TOML file to write to

    Raises:
        RuntimeError: if an unknown/unchecked exception occurs when writing to file
    """
    try:
        with open(toml_file_path, "w") as f:
            tomlkit.dump(toml_data, f)
            logger.debug("Successfully deserialized TOML data to '%s'", toml_file_path)
    except (EmptyKeyError, EmptyTableNameError) as ee:
        logger.exception("TOML file '%s' has invalid syntax", toml_file_path)
        raise ee
    except Exception as e:
        logger.exception("Could not deserialize to '%s' due to: ", toml_file_path)
        raise e


@validate_call
def get_value_from_key(
    toml_file_path: Annotated[str | Path, BeforeValidator(valid_toml_path_validator)],
    key_path: str = Field(..., min_length=1),
) -> str | list[str] | list[dict[str, object]]:
    """
    Get the value of a specific key from a given TOML file path.

    Args:
        toml_file_path (str | Path): the path to the TOML dict to get value from
        key_path (str): the path to the key in the specified language TOML dict

    Raises:
        PathAccessError: if the value could not be retrieved from the given key path
        FileNotFoundError: if the arg path to the TOML file does not exist
        RuntimeError: if an unknown/unchecked exception occurs when getting the value

    Returns:
        object: the value associated with the given key path
    """
    logger.debug("'key_path'=%r", key_path)
    try:
        language_toml_dict: dict[str, object] = serialize_toml_dict(toml_file_path)
        if value := glom(language_toml_dict, key_path):
            logger.debug(
                "Successfully retrieved '%s' with key '%s' from '%s'",
                value,
                key_path,
                toml_file_path,
            )
            return value
        logger.warning(
            "None retrieved with key '%s' from '%s'", key_path, toml_file_path
        )
        return [] if "*" in key_path else ""
    except PathAccessError as pae:
        logger.exception("Key '%s' does not exist in '%s'", key_path, toml_file_path)
        raise pae
    except Exception as e:
        logger.exception(
            "Could not get value with key '%s' from '%s' due to:",
            key_path,
            toml_file_path,
        )
        raise e
