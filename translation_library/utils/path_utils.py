import logging
from os.path import exists
from pathlib import Path

from pydantic import Field, validate_call

logger = logging.getLogger(__name__)


def valid_path_validator(v: str | Path) -> Path:
    """
    Checks to see if a given path exists and whether it is of type `str`
    or `Path`.

    Args:
        v (str | Path): a supposed `str`/`Path` path to a file

    Raises:
        ValueError: if a `str`/`Path` path was given and is was None/null
        FileNotFoundError: if a `str`/`Path` path was given and it did not exist

    Returns:
        Path: the original path if it exists, otherwise errors are raised.
    """
    logger.debug("path=%r", v)
    if isinstance(v, str):
        if not v.strip():
            logger.error("arg '%s' was None/null", v)
            raise ValueError("file path cannot be None/null")
        elif not exists(Path(v)):
            logger.error("arg '%s' could not be located/does not exist", v)
            raise FileNotFoundError(f"path '{v}' could not be located/does not exist")
        logger.info("Validated existence of path: %r", Path(v))
        return Path(v)

    if not exists(v):
        logger.error("arg '%s' could not be located/does not exist", v)
        raise FileNotFoundError(f"path '{v}' could not be located/does not exist")
    logger.info("Validated existence of path: %r", v)
    return v


@validate_call
def get_project_root(
    anchor: str = Field(default=".git", min_length=1),
) -> Path:
    """
    Find and return the path of the root path of the project.

    Args:
        anchor (str, optional): a known file/dir that exists in the project root. Defaults to ".git".

    Raises:
        FileNotFoundError: if `anchor` could not be found in parent dirs

    Returns:
        Path: the path of the project root
    """
    logger.debug("'anchor'=%r", anchor)
    current_path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / anchor).exists():
            logger.debug("found project root: %r", parent)
            return parent
    logger.error("'anchor' arg '%s' was not in parents of %s", anchor, current_path)
    raise FileNotFoundError(
        f"Could not find '{anchor}' in the parent dirs of '{current_path}'"
    )
