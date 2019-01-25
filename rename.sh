#!/bin/bash
i=1
for j in `ls ./pics/$1/*/*`
#for j in `ls $1`
do
	mv $j ./pics/$1/$1'__fanbingbing'$i.jpg
	i=$(expr $i + 1)
done

 
 
 
 
