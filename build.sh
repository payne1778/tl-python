#!/usr/bin/bash

set -e 

RESOURCES_DIR="resources"
TEMP_DIR="temp_resources_dir"
RESOURCES_REPO_NAME="Translation-Library-Docs"
RESOURCES_REPO_URL="https://github.com/payne1778/$RESOURCES_REPO_NAME"
COMMIT="main"

mkdir -p "$RESOURCES_DIR"
mkdir -p "logs" 

# Put contents of the docs repo into a new folder named with $DOCS_REPO_NAME
git subtree add --prefix="$TEMP_DIR/" "$RESOURCES_REPO_URL" "$COMMIT" --squash

mv "$TEMP_DIR/*" "$RESOURCES_DIR/"