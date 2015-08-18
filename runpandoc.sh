#!/bin/bash
find . -name \*.md -type f -exec bash -c 'pandoc -S -s -t html5 --self-contained -H ~/.pandoc/Assignments_style_header.html -o ${1%.md}.html $1' _ {} \;
