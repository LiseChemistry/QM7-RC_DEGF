#!/bin/bash

JOBNAME="QM7_hyperprm_regression"
TOT=$(cat $F_IN | wc -l)
MAX=900 
MULTI=100 
LEFT=$((TOT%MAX))

declare -a RANGES
for ((i=0;i<TOT;i+=MAX)); do
    RANGES+=("$i")
done
RANGES+=("$TOT")
NRANGE=${#RANGES[@]}

atom=("C" "H" "O" "N" "S") 
rep=("a_slatm" "a_spahm" "b_spahm") 
seed=("1" "2" "3") 

echo "Starting submissions! (Tot. Jobs = ${TOT})"

for atom in "${atoms[@]}"; do
    for representation in "${representations[@]}"; do
        for seed in "${seeds[@]}"; do
            for ((i=1; i<NRANGE; i++)); do
                SHIFT=$(((i-1)*${MAX}))
                FROM=${RANGES[$((i-1))]}
                TO=${RANGES[$i]}
                TO=$((TO-1))
                
                while :
                do
                    RUNS=$(squeue -u student5 -n $JOBNAME --array -h | wc -l)
                    echo "Tâches en cours: $RUNS"
                    if [[ $RUNS -lt $((${MAX}-${MULTI}-5)) ]]; then 
                        break
                    fi
                    sleep 30
                done

                echo "Soumission de l'array pour ${atom} ${rep} ${seed} de: ${FROM} à: ${TO}"
                sbatch -J ${JOBNAME} --array=$((FROM-SHIFT))-$((TO-SHIFT))%${MULTI} hyperparameters_regression.py $SHIFT $atom $rep $seed
            done
        done
    done
done

