#!/bin/bash

i=1
for f in `ls`
do
	if [ -d $f ]
	then
		#echo $f
		rm -rf $f
	fi
done
