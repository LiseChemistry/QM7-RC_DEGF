#!/bin/bash
#SBATCH -n 1
#SBATCH -c 2
#SBATCH --mem 5GB

SHIFT=$1

molist=($(cat list_all_neutral.txt))
echo "Found ${#molist[@]} molecules!"

SLURM_ARRAY_TASK_ID=$((SLURM_ARRAY_TASK_ID+SHIFT))
molname=${molist[$SLURM_ARRAY_TASK_ID]}
echo $molname

eval "$(conda shell.bash hook)"
conda activate myenv

python example_compute_a_spahm.py "/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/opt_neutral_xyz/xyz_opt_0_1/${molname}.xyz"
