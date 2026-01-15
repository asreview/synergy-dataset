#!/usr/bin/env bash
set -e

for dir in ../datasets/*/; do
    ( cd "$dir" && python compose.py )
done