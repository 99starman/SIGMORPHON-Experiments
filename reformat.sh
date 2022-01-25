#!/bin/bash

LANGUAGE=$1


echo $LANGUAGE

python3 reformat_for_eval.py $LANGUAGE

echo "end reformatting $LANGUAGE"

