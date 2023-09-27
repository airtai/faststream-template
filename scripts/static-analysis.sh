#!/bin/bash
set -e

echo "Running mypy..."
mypy app

echo "Running bandit..."
bandit -c pyproject.toml -r app
