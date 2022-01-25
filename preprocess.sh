#!/bin/bash

LANGUAGE=$1
DATADIR="data-bin/${LANGUAGE}"

python3 fairseq_format.py $LANGUAGE

fairseq-preprocess \
    --source-lang="${LANGUAGE}.input" \
    --target-lang="${LANGUAGE}.output" \
    --trainpref=train \
    --validpref=dev \
    --testpref=test \
    --tokenizer=space \
    --thresholdsrc=1 \
    --thresholdtgt=1 \
    --destdir="data-bin/${LANGUAGE}/"
    
mv *".${LANGUAGE}."* $DATADIR