#! /bin/bash

x=$(ls)

for i in ${x[@]}
do
    echo $i
done
