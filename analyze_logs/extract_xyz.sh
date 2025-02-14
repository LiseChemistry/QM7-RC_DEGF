#!/usr/bin/env bash
## This script is used to extract all geometries form Gaussian log files

function get_cooord(){
	logfile=$1
	start=$2
	coords=()
	tot=0
	#pattern=[0-9]+\s+[0-9]+\s+[0-9]+\s+[0-9\-.]+\s+[0-9\-.]+\s+[0-9\-.]+
	pattern=" *[0-9]+ +([0-9]+) +[0-9]+ +(-?[0-9.]+) +(-?[0-9.]+) +(-?[0-9.]+) *"
	while IFS="\n" read line; do
		if [[ "$line" =~ $pattern ]];then
			q=${symbols[${BASH_REMATCH[1]}]}
			x=${BASH_REMATCH[2]}
			y=${BASH_REMATCH[3]}
			z=${BASH_REMATCH[4]}
			coords+=("$q $x $y $z")
			tot=$(($tot+1))
		else
			break	
		fi
	done < <(sed -n "${start},\$p" $logfile)
}

function write_xyz(){
	geom=$coords
	natm=$tot
	echo $natm
	echo ""
	for il in ${!coords[@]};do
		echo ${coords[$il]}
	done
}

declare -A symbols=(["1"]="H" ["6"]="C" ["7"]="N" ["8"]="O" ["16"]="S")
fin=$1

strpos=()

reg=([0-9]*):.*
while IFS="\n" read line;do
	if [[ "$line" =~ $reg ]];then
		strpos+=(${BASH_REMATCH[1]})
	else
		echo "Output does not match pattern!"
		echo "Exiting!"
		exit 1
	fi
done < <(grep "Input orientation" $fin -n)

#echo ${strpos[@]}

ngeom=0
for s in ${strpos[@]};do
	molname=${fin##*/}
	molname=${molname%.log}
	get_cooord $fin $(($s+5))
	write_xyz > "${ngeom}-${molname}.xyz"
	echo "Extracted geomtry ${ngeom}"
	ngeom=$(($ngeom+1))
done

