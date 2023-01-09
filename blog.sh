#!/bin/sh
#shopt -s expand_aliases extglob
#alias edit="micro -filetype markdown"

cd ~/Documenti/blog

python3 blog.py $@

cd ~/
