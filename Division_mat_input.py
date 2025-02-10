import os
import numpy as np
from collections import Counter
from scipy.io import loadmat

input_file = '/home/student/Documents/QM7/qm7.mat'
output_dir = '/home/student/Documents/QM7/data_molecules'
os.makedirs(output_dir, exist_ok=True)

data = loadmat(input_file)

Z = data['Z']  #atomic_numbers
R = data['R']  #atomic_coordinates

n_molecules = Z.shape[0]
molecule_count = 0

atomic_symbols = {
    1: "H",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    15: "P",
    16: "S",
    17: "Cl",
    35: "Br",
    53: "I"
}

for i in range(n_molecules):
    atomic_numbers = Z[i].flatten()
    mask = atomic_numbers > 0
    atoms = atomic_numbers[mask]
    
    if R.ndim == 3:
        positions = R[i][mask]  
    elif R.ndim == 2:
        max_atoms = R.shape[1] // 3
        positions = R[i].reshape((max_atoms, 3))[mask] 
    else:
        raise ValueError("Format inattendu pour la variable R dans le fichier MAT.")

    num_atoms = len(atoms)
    if num_atoms == 0:
        continue 
    atom_counts = Counter(atomic_symbols.get(int(num), str(num)) for num in atoms)

    filename = f"mol_{i:04d}"
    file_content = []

    file_content.append(f'%chk={filename}.chk\n')  
    file_content.append('# wB97XD/Def2SVP opt pop=full gfinput\n')
    file_content.append('\n')  

    atom_counts_line = " ".join(f"{element} {count}" for element, count in sorted(atom_counts.items()))
    file_content.append(f"{atom_counts_line}\n")

    file_content.append('\n')  
    file_content.append("1 2\n")

    for j, num in enumerate(atoms):
        symbole = atomic_symbols.get(int(num), str(num))
        x, y, z_coord = positions[j]
        file_content.append(f"{symbole:<2} {x:10.6f} {y:10.6f} {z_coord:10.6f}\n")
    file_content.append('\n')  
    filepath = os.path.join(output_dir, f"{filename}.inp")
    with open(filepath, "w") as mol_file:
        mol_file.writelines(file_content)

    molecule_count += 1

print(f"{molecule_count} molécules extraites et enregistrées dans {output_dir}/")