#!/bin/bash
#SBATCH -n 1
#SBATCH -c 2
#SBATCH --mem 5GB


SHIFT=$1

molist=($(cat good_logs_list.txt))
echo "Found ${#molist[@]} molecules!"

SLURM_ARRAY_TASK_ID=$((SLURM_ARRAY_TASK_ID+SHIFT))
molname=${molist[$SLURM_ARRAY_TASK_ID]}
echo $molname

eval "$(conda shell.bash hook)"
conda activate myenv

python example_compute_a_spahm.py "QM7_RC_optimized_xyz/${molname}.xyz"
