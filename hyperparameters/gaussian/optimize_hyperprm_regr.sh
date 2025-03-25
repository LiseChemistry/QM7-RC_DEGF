#!/bin/bash

JOBNAME="QM7_hyperprm_regression"

atoms=("C" "H" "O" "N" "S")
reps=("a_slatm" "a_spahm" "b_spahm")
seeds=("1" "2" "3" "4" "5")

for atom in "${atoms[@]}"; do
    for rep in "${reps[@]}"; do
        for seed in "${seeds[@]}"; do
            sbatch --job-name=$JOBNAME --wrap="python3 hypereparameters_regression.py $atom $rep $seed"
        done
    done
done

