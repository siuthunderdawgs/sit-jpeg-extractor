#!/bin/bash

shopt -s nullglob
for f in *.SIT
do
	echo "Processing $f file...."
	python extract_jpeg.py $f
done
