#!/bin/bash

faststream docs gen --yaml app.application:app

npx -y -p @asyncapi/generator ag asyncapi.yaml @asyncapi/html-template -o asyncapi_docs

python -m http.server --directory asyncapi_docs 8888
