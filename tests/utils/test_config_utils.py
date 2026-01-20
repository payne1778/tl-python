import pytest
from glom.core import PathAccessError  # type: ignore

from resources.constants.values import (
    EXAMPLE_SUPPORTED_LANGUAGE,
    EXAMPLE_SUPPORTED_LANGUAGE_CODE,
    EXAMPLE_UNSUPPORTED_LANGUAGE,
    EXAMPLE_UNSUPPORTED_LANGUAGE_CODE,
)
from translation_library.utils.config_utils import (
    get_all_english_names,
    get_all_file_names,
    get_all_language_codes,
    get_all_native_names,
    get_config_file_path,
    get_fallback_language_code,  # TODO: test this
    get_i18n_dir_path,
    get_language_file_path,
    get_value_from_config,  # TODO: test this
    language_code_to_english_name,
    language_code_to_file_name,  # TODO: test this
    language_code_to_native_name,
)


def test_get_config_file_path() -> None:
    assert get_config_file_path().exists()


# def test_get_value_from_config() -> None:


def test_get_i18n_dir_path() -> None:
    assert get_i18n_dir_path().exists()


def test_get_all_english_names() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE.casefold() in [
        name.casefold() for name in get_all_english_names()
    ]


def test_get_all_native_names() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE.casefold() in [
        name.casefold() for name in get_all_native_names()
    ]


def test_get_all_file_names() -> None:
    for file in get_all_file_names():
        if file.__contains__(EXAMPLE_SUPPORTED_LANGUAGE) or file.__contains__(
            EXAMPLE_SUPPORTED_LANGUAGE_CODE
        ):
            return
    raise ValueError(
        "Could not verify if the supported language as an associated TOML file"
    )


def test_get_all_file_names_fail() -> None:
    for file in get_all_file_names():
        if file.__contains__(EXAMPLE_UNSUPPORTED_LANGUAGE) or file.__contains__(
            EXAMPLE_UNSUPPORTED_LANGUAGE_CODE
        ):
            raise ValueError(
                "Found an associated TOML file for an unsupported language"
            )
    return


def test_get_all_language_codes() -> None:
    assert EXAMPLE_SUPPORTED_LANGUAGE_CODE in get_all_language_codes()


def test_language_code_to_english_name() -> None:
    assert (
        language_code_to_english_name(code=EXAMPLE_SUPPORTED_LANGUAGE_CODE).casefold()
        == EXAMPLE_SUPPORTED_LANGUAGE.casefold()
    )


def test_language_code_to_english_name_fail() -> None:
    with pytest.raises(PathAccessError):
        _ = language_code_to_english_name(EXAMPLE_UNSUPPORTED_LANGUAGE_CODE)


def test_language_code_to_native_name() -> None:
    assert (
        language_code_to_native_name(EXAMPLE_SUPPORTED_LANGUAGE_CODE).casefold()
        == EXAMPLE_SUPPORTED_LANGUAGE.casefold()
    )


def test_language_code_to_native_name_fail() -> None:
    with pytest.raises(PathAccessError):
        _ = language_code_to_native_name(EXAMPLE_UNSUPPORTED_LANGUAGE_CODE)


# def test_language_code_to_file_name() -> None:


def test_get_language_file_path() -> None:
    assert get_language_file_path(EXAMPLE_SUPPORTED_LANGUAGE_CODE).exists()
