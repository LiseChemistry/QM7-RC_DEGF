#!/bin/bash

ZPEfile="ZPE.txt"

E_0file="E_0.txt"

mol_list="/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/good_logs_list.txt"

while IFS= read -r molname; do
    logfile="/home/student5/lise/MasterProject_SPAHM-ENN/QM7_RC_optimized_log/${molname}.log"
    if [[ -f "$logfile" ]]; then	
	export string=$(grep "SCF Done:  E(UwB97XD) =" "$logfile" | tail -n 1)
	if [[ "$string" =~ -?[0-9]+\.[0-9]+ ]];then
		echo "Total energy (A.U.): ${BASH_REMATCH[0]}";
		total_energy_AU=${BASH_REMATCH[0]}
		echo "Total energy (A.U.): $total_energy_AU"
		total_energy_kcal=$(echo "$total_energy_AU * 627.51" | bc -l)
        	echo "Total energy (Kcal/Mol): $total_energy_kcal"
        	echo "$total_energy_kcal" >> "$E_0file";
        fi

	export string=$(grep "Zero-point vibrational energy" "$logfile" -n)
	echo ${string%%:*}
	export line="${string%%:*}"
	echo $(($line+1))
	export new_line=$(($line+1)) 
	export ll=$(sed -n "${new_line}p" "$logfile")
	if [[ "$ll" =~ [0-9\.]+ ]];then
		echo "Zero-point vibrational energy (Kcal/Mol): ${BASH_REMATCH[0]}";
		echo ${BASH_REMATCH[0]} >> "$ZPEfile";
	fi 
    fi

done < "$mol_list"

