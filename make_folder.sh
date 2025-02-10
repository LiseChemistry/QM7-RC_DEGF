#!/bin/bash


molnames=($(ls ./data_molecules/))

#echo "${molnames[@]}"
echo ${#molnames[@]}

for f in ${molnames[@]};do
	dirname=${f%.inp}
	mkdir --parents ./opt/${dirname}/
	cp ./data_molecules/${f} ./opt/${dirname}/
done


