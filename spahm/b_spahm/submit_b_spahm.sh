#!/bin/bash

F_IN="./good_logs_list.txt"

JOBNAME="QM7_b_spahm"

TOT=$(cat $F_IN | wc -l)

MAX=900 ### le nombre maximum de jpob dans le array
MULTI=100 ## le nombre de job a faire tourner en parallele

LEFT=$((TOT%MAX))

declare -a RANGES
for ((i=0;i<TOT;i+=MAX)); do
	RANGES+=("$i")
done
RANGES+=("$TOT")
NRANGE=${#RANGES[@]}

echo "Starting submissions ! (Tot. Jobs  = ${TOT})"
for ((i=1;i<NRANGE;i++)); do
	SHIFT=$(((i-1)*${MAX}))
	FROM=${RANGES[$((i-1))]}
	TO=${RANGES[$i]}
	TO=$((TO-1))
	while :
	do
		RUNS=$(squeue -u student5 -n $JOBNAME --array -h | wc -l)
		echo $RUNS
	if [[ $RUNS -lt $((${MAX}-${MULTI}-5)) ]]; then # alternative check that the number of runs is smaller thant the max number of simultaneous jobs !!!
			break
		fi
		sleep 30
	done
	echo "Submitting array from: ${FROM} to: ${TO}"
	sbatch -J ${JOBNAME} --array=$((FROM-SHIFT))-$((TO-SHIFT))%${MULTI} compute_b_spahm.sbatch $SHIFT
done
