#!/bin/bash

function rand(){
    min=$1
    max=$(($2-$min+1))
    num=$(date +%s%N)
    echo $(($num%$max+$min))
}

function commit_once(){
    python3 _main.py
    git add .
    git commit -m "update `date` $RANDOM"
}

commit_cnt=$(rand 1 9)
for ((i=0;i<=$commit_cnt;i+=1))
   do
     commit_once
   done

git pull origin master
git push origin master
