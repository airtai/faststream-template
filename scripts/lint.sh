#!/bin/bash

echo "Running pyup_dirs..."
pyup_dirs --py38-plus --recursive app tests

echo "Running ruff..."
ruff app tests --fix

echo "Running isort..."
isort app tests

echo "Running black..."
black app tests
