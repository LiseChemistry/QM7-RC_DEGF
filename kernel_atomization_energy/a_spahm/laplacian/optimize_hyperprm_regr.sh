#!/bin/bash

seeds=("1" "2" "3" "4" "5")

for seed in "${seeds[@]}"; do
    JOBNAME="${seed}_QM7_a_spahm_hyperprm"
    sbatch --job-name=$JOBNAME --mem=60GB -n 1 -c 2 --wrap="conda run -n new-q-stack --live-stream python hyperparameters_regression.py $seed"
done
