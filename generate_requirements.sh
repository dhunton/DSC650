#!/usr/bin/env bash

# shellcheck disable=SC2094
poetry export -f requirements.txt --without-hashes --dev > requirements.txt
