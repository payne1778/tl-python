#!/usr/bin/bash

set -e 

RESOURCES_DIR="resources"
RESOURCES_REPO_NAME="Translation-Library-Docs"
RESOURCES_REPO_URL="https://github.com/payne1778/$RESOURCES_REPO_NAME"
COMMIT="main"

# Put contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$RESOURCES_DIR/" "$RESOURCES_REPO_URL" "$COMMIT" --squash