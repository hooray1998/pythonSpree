#!/bin/bash
i=1
for j in `ls $1`
do
	echo $1/$j $1/$1$i.jpg
	i=$(expr $i + 1)
done

 
 
 
 
