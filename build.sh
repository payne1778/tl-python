#!/usr/bin/bash

set -e 

# 1. Create important dirs (if they do not already exist)
LOGS_DIR="logs"
RESOURCES_DIR="resources"

mkdir -p "$RESOURCES_DIR"
mkdir -p "$LOGS_DIR" 

# 2. Clone resources repo into a new folder named with $RESOURCES_REPO_NAME
RESOURCES_REPO_NAME="Translation-Library-Docs"
RESOURCES_REPO_URL="https://github.com/payne1778/$RESOURCES_REPO_NAME"
COMMIT="main"

git subtree add --prefix="$RESOURCES_REPO_NAME" "$RESOURCES_REPO_URL" "$COMMIT" --squash

# 3. Move resources repo files into the resource directory
mv "$RESOURCES_REPO_NAME"/* "$RESOURCES_DIR"/

# 4. Delete the (should be) empty temp folder 
rm -rf "$RESOURCES_REPO_NAME"