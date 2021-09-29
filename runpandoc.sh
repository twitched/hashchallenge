#!/bin/bash
find . -name \*.md -type f -exec bash -c 'pandoc -s -f markdown -t html5 --self-contained --css style.css -o ${1%.md}.html $1;' _ {} \;
