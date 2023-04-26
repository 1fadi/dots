#!/bin/bash
#
# This script copies all files from this directory to ~/

echo "creating directories in $HOME..."
find . -type d -not -path './.git' -print -exec mkdir -pv ~/{} \;
echo "copying files to destination..."
find . -type f -not -path './.gitignore' -print -exec cp -av '{}' ~/{} \;
echo "All setup!"
