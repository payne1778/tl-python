"""
const values used primarily by unit tests
"""

from pathlib import Path

PARENT_DIR_PATH = Path(__file__).resolve().parent

EXAMPLE_UNSUPPORTED_LANGUAGE = "warlpiri"

EXAMPLE_SUPPORTED_LANGUAGE = "english"

EXAMPLE_SUPPORTED_LANGUAGE_CODE: str = "en"

EXAMPLE_UNSUPPORTED_LANGUAGE_CODE: str = "wbp"

EXAMPLE_UNSUPPORTED_LANGUAGE_TOML_PATH: Path = Path(
    f"{EXAMPLE_UNSUPPORTED_LANGUAGE}.toml"
)

EXAMPLE_UNSUPPORTED_FILE_EXTENSION_PATH: Path = PARENT_DIR_PATH / "example.json"

EXAMPLE_INVALID_TOML_SYNTAX_PATH: Path = PARENT_DIR_PATH / "invalid.toml"

EXAMPLE_ENGLISH_TOML_PATH: Path = PARENT_DIR_PATH / "example.toml"

# Note: there are some hard coded of accessing this specific TOML dict
EXAMPLE_ENGLISH_TOML_DICT: dict[str, object] = {
    "setting": "This is the English language file",
    "hello": "Hello {name}",
    "start": {
        "section_name": "This message is under the start section",
        "welcome": "Welcome {name}!",
    },
}
