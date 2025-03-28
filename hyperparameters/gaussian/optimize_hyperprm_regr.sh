#!/bin/bash

JOBNAME="QM7_hyperprm_regression"

atoms=("C" "H")
reps=("a_slatm" "a_spahm" "b_spahm")
seeds=("1" "2" "3" "4" "5")

#eval "$(conda shell.bash hook)"
#conda activate myenv

for atom in "${atoms[@]}"; do
    for rep in "${reps[@]}"; do
        for seed in "${seeds[@]}"; do
            sbatch --job-name=$JOBNAME --mem=48GB -n 1 -c 2 --wrap="conda run -n new-q-stack --live-stream python hyperparameters_regression.py $atom $rep $seed"
        done
    done
done
