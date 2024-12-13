#!/bin/bash
rm -f testexam.txt
for sol in vuoto iac;
do
    echo ">> testing solution:" $sol "..."
    echo $sol >> testexam.txt
    ln -sf program.$sol.py program.py;
    score=`python grade.py | grep "Total score"`
    echo $score
    echo $score >> testexam.txt
    echo ">> tested solution:" $sol "!"
done
