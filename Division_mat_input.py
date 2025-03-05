#!/usr/bin/env python3

import os
import numpy as np
from collections import Counter
from scipy.io import loadmat

input_file = './qm7.mat'
output_dir = './data_molecules'

data = loadmat(input_file)

Z = data['Z']  
R = data['R'] 

n_molecules = Z.shape[0]
molecule_count = 0

atomic_symbols = {
    1: "H", 6: "C", 7: "N", 8: "O", 9: "F",
    15: "P", 16: "S", 17: "Cl", 35: "Br", 53: "I"
}

bohr_to_angstrom = 0.529177

for i in range(n_molecules):
    atomic_numbers = Z[i].flatten()
    mask = atomic_numbers > 0 
    atoms = atomic_numbers[mask]
    
    if R.ndim == 3:
        positions = R[i][mask]  
    else:
        raise ValueError("Does not fit the format for variable R in file MAT.")

    positions *= bohr_to_angstrom  

    num_atoms = len(atoms)
    if num_atoms == 0:
        continue 

    atom_counts = Counter(atomic_symbols.get(int(num), str(num)) for num in atoms)

    filename = f"mol_{i:04d}"
    file_content = []

    file_content.append(f'%chk={filename}.chk\n')  
    file_content.append('# wB97XD/Def2SVP opt freq pop=full gfinput\n') # wB97XD/Def2SVP opt freq pop=full gfinput
    file_content.append('\n')  

    atom_counts_line = " ".join(f"{element} {count}" for element, count in sorted(atom_counts.items()))
    file_content.append(f"{atom_counts_line}\n")

    file_content.append('\n')  
    file_content.append("1 2\n")

    for j, num in enumerate(atoms):
        symbole = atomic_symbols.get(int(num), str(num))
        x, y, z_coord = positions[j]
        file_content.append(f"{symbole:<2} {x:12.8f} {y:12.8f} {z_coord:12.8f}\n")  

    file_content.append('\n')  
    filepath = os.path.join(output_dir, f"{filename}.inp")
    with open(filepath, "w") as mol_file:
        mol_file.writelines(file_content)

    molecule_count += 1

print(f"{molecule_count} molecules saved in {output_dir}/")
