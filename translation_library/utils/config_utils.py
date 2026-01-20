# mypy: ignore-errors

import logging
from pathlib import Path

from translation_library.utils.path_utils import get_project_root
from translation_library.utils.toml_utils import get_value_from_key

logger = logging.getLogger(__name__)


def get_config_file_path() -> Path:
    return get_project_root() / "config.toml"


def get_value_from_config(
    key_path: str,
) -> str | list[str] | list[dict[str, object]]:
    return get_value_from_key(get_config_file_path(), key_path)


def get_i18n_dir_path() -> Path:
    return Path(str(get_value_from_config("paths.i18n_dir")))


def get_fallback_language_code() -> str:
    return str(get_value_from_config("languages.fallback"))


def get_all_english_names() -> list[str]:
    return [str(name) for name in get_value_from_config("languages.*.english_name")]


def get_all_native_names() -> list[str]:
    return [str(name) for name in get_value_from_config("languages.*.native_name")]


def get_all_file_names() -> list[str]:
    return [str(name) for name in get_value_from_config("languages.*.file")]


def get_all_language_codes() -> list[str]:
    return [code for code in get_value_from_config("languages").keys()]


def language_code_to_english_name(code: str) -> str:
    return str(get_value_from_config(f"languages.{code.lower()}.english_name"))


def language_code_to_native_name(code: str) -> str:
    return str(get_value_from_config(f"languages.{code.lower()}.native_name"))


def language_code_to_file_name(code: str) -> str:
    return str(get_value_from_config(f"languages.{code.lower()}.file"))


def get_language_file_path(code: str) -> Path:
    return get_i18n_dir_path() / Path(
        str(get_value_from_config(f"languages.{code.lower()}.file"))
    )
