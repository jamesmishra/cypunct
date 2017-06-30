#!/bin/bash

# This is the standard linting script for development.
# It will mutate your existing source code to
# make it pep8 compliant and nicely formatted.

# Check that we are running inside a virtualenv.
if [ -z $VIRTUAL_ENV ]
then
    echo "Run linter inside virtualenv."
    exit 1
fi

# Check that all linters are installed locally.
LINTERS=( autoflake isort autopep8 pycodestyle pydocstyle pylint mypy)
for SOME_CMD in "${LINTERS[@]}"
do
    which $SOME_CMD | grep $VIRTUAL_ENV > /dev/null
    if [ $? -ne 0 ]
    then
        echo "Missing linter $SOME_CMD"
        exit 1
    fi
done

# Lint away.
# First we remove unused imports and variables
echo "[lint] Running autoflake..."
find cypunct -name '*.py' -exec autoflake --in-place --remove-unused-variables  --remove-all-unused-imports {} \;
# Then we sort our imports
echo "[lint] Running isort..."
isort -sl --recursive --quiet cypunct
# We do some automated pep8 cleanup.
# This reduces complaints from pylint later on.
echo "[lint] Running autopep8..."
autopep8 --in-place --recursive --aggressive --aggressive cypunct
# Figure out if we wrote our docstrings poorly.
echo "[lint] Running pydocstyle..."
pydocstyle cypunct
# Get some feedback on Python code style.
echo "[lint] Running pycodestyle..."
pycodestyle cypunct
# Check that everything is appropriately typed.
echo "[lint] Running mypy..."
mypy --ignore-missing-imports --strict-optional --check-untyped-defs cypunct
# Check for all sorts of errors.
echo "[lint] Running pylint..."
pylint cypunct
