#!/bin/bash

TYPE=tst
LANGUAGE=$1

echo $LANGUAGE
python task0-data/evaluate.py --hyp "formatted_prediction/${LANGUAGE}.output" --ref "task0-data/GOLD-TEST/${LANGUAGE}.${TYPE}" 
echo "end eval"

