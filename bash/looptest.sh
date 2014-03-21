#!/bin/bash

start=1007
end=1215
batch_size=10

i=$start

while [[ $i -lt $end ]]; do
     #statements

     server=()

     start_range=$i
     end_range=$i+$batch_size

     end_range=$(($end_range<$end?$end_range:$end))

     for (( j = $start_range; j <= $end_range; j++ )); do
         server+=($j)
     done

     echo $server

     i=$((i + batch_size))
 done