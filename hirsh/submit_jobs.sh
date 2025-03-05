#!/bin/bash

JOBNAME="python_parallel_job"
SCRIPT_PATH="/home/student/MasterProject_SPAHM-ENN/hirsh/code.py"  
LOGS_LIST="/home/student/MasterProject_SPAHM-ENN/logs_list.txt"    
MULTI=20 

if [[ ! -f "$LOGS_LIST" ]]; then
    echo "Erreur : le fichier $LOGS_LIST n'existe pas."
    exit 1
fi

mapfile -t file_list < "$LOGS_LIST"

for i in "${!file_list[@]}"; do
    if (( i % MULTI == 0 )); then
        echo "Soumettre un groupe de 10 jobs"
    fi

    sbatch --job-name=$JOBNAME \
           --output="/home/student/MasterProject_SPAHM-ENN/hirsh/job_${i}.out" \
           --error="/home/student/MasterProject_SPAHM-ENN/hirsh/job_${i}.err" \
           --ntasks=1 --cpus-per-task=1 \
           --wrap="python3 $SCRIPT_PATH ${file_list[$i]}"

    if (( (i + 1) % MULTI == 0 )); then
        sleep 1
    fi
done

echo "Tous les jobs ont été soumis."

