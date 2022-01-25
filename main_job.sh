#!/bin/bash
# main script that calls a slurm job

# LANGUAGE=$1

# low-resource (< 5000 trn ex): ceb(w/ 1src), gaa(w/ 1src), swa, ctp, zpv
# ceb gaa dan deu krl fin nld swe swa ctp zpv
# assuming data-bin/alpha.all pre-exists

# try deu
for LANGUAGE in deu; do
  
  echo "... start ..."
  echo $LANGUAGE  
  
  FOLDER="data-bin/${LANGUAGE}"
  FILE="data-bin/${LANGUAGE}_map.txt"
  
  echo "... get data ..."
  echo "----start $LANGUAGE time----" >> results.txt
  date >> results.txt
  
  if [ ! -d "$FOLDER" ]; then
      echo "start new"
      mkdir -p "$FOLDER"
      bash preprocess.sh $LANGUAGE
  fi
      
  if [ ! -f "$FILE" ]; then
      echo "build map"
      python3 build_map.py $LANGUAGE
  fi
    
  echo "... training models ..."
  bash train.sh $LANGUAGE 10000
   
  echo "... generating and evaluating for dev set ..."
  bash generate.sh $LANGUAGE dev
  
  # continue training for another 10000 updates, select best five model on dev so far
  echo "... training models ..."
  bash train.sh $LANGUAGE 20000
  
  echo "... generating and evaluating for dev set ..."
  bash generate.sh $LANGUAGE dev 
  
  echo "----end $LANGUAGE dev time----" >> results.txt
  date >> results.txt
  
  # generate for test data
  echo "... generating and evaluating for test set ..."
  bash generate.sh $LANGUAGE test 
  
  echo "... reformat for eval ..."
  bash reformat.sh $LANGUAGE
  
  echo " ... eval ..."
  bash evaluate.sh $LANGUAGE >> results.txt
  
  echo "... end language $LANGUAGE ..."
  echo "----end $LANGUAGE time----" >> results.txt
  date >> results.txt

done

echo "end script"