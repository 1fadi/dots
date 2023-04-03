#!/bin/bash

# A script that synchronizes a source directory with 
# a destination directory by copying all files and subdirectories, 
# excluding the ones specified in the "EXCLUDE" argument.

while [[ $# -gt 0 ]]
do
	case $1 in
		-e) EXCLUDE="$2"
			shift
			shift
			;;
		-d) DESTINATION="$2"
			shift
			shift
			;;
		*) source_dir=$1
			shift
			;;
	esac
done

cd $source_dir && find . -type d -not -path */"${EXCLUDE}"/* -print -exec mkdir -p /"${DESTINATION}"/'{}' \;

cd $source_dir && find . -type f -not -path */"${EXCLUDE}"/* -print -exec cp -au '{}' /"${DESTINATION}"/'{}' \;
