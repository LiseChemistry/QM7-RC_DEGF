#!/bin/bash

atoms=("S" "N" "O")
reps=("a_slatm" "a_spahm" "b_spahm")
seeds=("1" "2" "3" "4" "5")

for atom in "${atoms[@]}"; do
    for rep in "${reps[@]}"; do
        for seed in "${seeds[@]}"; do
            JOBNAME="${atom}-${rep}-${seed}_QM7_hyperprm"
            sbatch --job-name=$JOBNAME --mem=60GB -n 1 -c 2 --wrap="conda run -n new-q-stack --live-stream python hyperparameters_regression.py $atom $rep $seed"
        done
    done
done
