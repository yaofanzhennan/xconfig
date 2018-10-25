#!/bin/bash


function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(date +%s%N)
    echo $(($num%$max+$min))
}

rnd=$(rand 1 50)

python3 _main.py
git pull origin master
git add .
echo $rnd
git commit -m "update $rnd"
git push origin master
