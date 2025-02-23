#!/bin/bash
#SBATCH -n 1
#SBATCH -c 2
#SBATCH --mem 5GB

molname="Atom_en_O"

inputdir="/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/${molname}"

inputfile="${molname}.inp"

module load gaussian/g16/C.01

cd $inputdir

g16 -p=2 ${inputfile}


