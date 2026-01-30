import pytest
from glom.core import PathAccessError  # type: ignore
from pydantic_core import ValidationError
from tomlkit.exceptions import EmptyKeyError, EmptyTableNameError

from resources.constants.values import (
    EXAMPLE_ENGLISH_TOML_DICT,
    EXAMPLE_ENGLISH_TOML_PATH,
    EXAMPLE_INVALID_TOML_SYNTAX_PATH,
    EXAMPLE_UNSUPPORTED_FILE_EXTENSION_PATH,
    EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH,
)
from tl.utils.toml_utils import (
    deserialize_toml_dict,
    get_value_from_key,
    serialize_toml_dict,
    valid_toml_path_validator,  # TODO: test this
)


def test_serialize_toml() -> None:
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_serialize_toml_wrong_extension_fail() -> None:
    with pytest.raises(ValueError):
        _ = serialize_toml_dict(EXAMPLE_UNSUPPORTED_FILE_EXTENSION_PATH)


def test_serialize_toml_invalid_toml_syntax_fail() -> None:
    with pytest.raises((ValueError, EmptyKeyError, EmptyTableNameError)):
        _ = serialize_toml_dict(EXAMPLE_INVALID_TOML_SYNTAX_PATH)


def test_deserialize_toml() -> None:
    deserialize_toml_dict(EXAMPLE_ENGLISH_TOML_DICT, EXAMPLE_ENGLISH_TOML_PATH)
    assert serialize_toml_dict(EXAMPLE_ENGLISH_TOML_PATH) == EXAMPLE_ENGLISH_TOML_DICT


def test_deserialize_toml_wrong_extension_fail() -> None:
    with pytest.raises(ValueError):
        deserialize_toml_dict(
            EXAMPLE_ENGLISH_TOML_DICT, EXAMPLE_UNSUPPORTED_FILE_EXTENSION_PATH
        )


def test_deserialize_toml_empty_dict_fail() -> None:
    with pytest.raises(ValidationError):
        deserialize_toml_dict({}, EXAMPLE_ENGLISH_TOML_PATH)


def test_get_value_from_key_pass() -> None:
    _ = get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="setting")


def test_get_value_from_key_nested_key_pass() -> None:
    _ = get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="start.section_name")


def test_get_value_from_key_empty_str_path_fail() -> None:
    with pytest.raises(ValidationError):
        _ = get_value_from_key("", key_path="hello")


def test_get_value_from_key_empty_key_path_fail() -> None:
    with pytest.raises(ValidationError):
        _ = get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="")


def test_get_value_from_key_wrong_section_fail() -> None:
    with pytest.raises(PathAccessError):
        _ = get_value_from_key(EXAMPLE_ENGLISH_TOML_PATH, key_path="welcome")


def test_get_value_from_key_unsupported_language_fail() -> None:
    with pytest.raises(FileNotFoundError):
        _ = get_value_from_key(EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH, key_path="hello")
