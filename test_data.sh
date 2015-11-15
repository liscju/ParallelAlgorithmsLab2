#!/usr/bin/env bash

SIZES_OF_ARRAY=("1000" "10000" "100000" "1000000" "10000000" "100000000" "1000000000")
COUNT_OF_PROCS=("2" "10" "15" "20" "25" "30" "35")


for i in 0 1 2 3 4 5 6
do
    OUTFILE="parralel_algorithm_${SIZES_OF_ARRAY[$i]}_${COUNT_OF_PROCS[$i]}"
    touch $OUTFILE
    for k in 1 2 3 4 5 6 7 8 9 10
    do
        CALC_TIME=$(TIMEFORMAT="%R"; { time ./run.sh seq ${SIZES_OF_ARRAY[$i]}; }  2>&1 )
        echo "sequential=${CALC_TIME}\n" >> $OUTFILE
    done 
    for k in 1 2 3 4 5 6 7 8 9 10
    do
        CALC_TIME=$(TIMEFORMAT="%R"; { time ./run.sh par ${SIZES_OF_ARRAY[$i]} ${COUNT_OF_PROCS[$i]}; }  2>&1 )
        echo "parallel=${CALC_TIME}\n" >> $OUTFILE
    done 
done

