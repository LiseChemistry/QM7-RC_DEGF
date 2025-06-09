#!/usr/bin/env python3

import numpy as np
import os

atoms_file = 'list_atoms.txt'
log_list = 'list_mixed_data.txt'
representations = ["slatm"]
directories = {
    "slatm": "/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/mixed_slatm/results",
}
atoms_list = ['C', 'H', 'S', 'O', 'N']
atom_order = np.loadtxt(atoms_file, dtype=str)

with open(log_list, 'r', encoding='utf-8') as file:
    list_names = [line.strip() for line in file]

for rep in representations:
    atom_to_file = {atom: [] for atom in atoms_list}
    rep_data = []

    for file_name in list_names:
        file_path = os.path.join(directories[rep], f"{file_name}.npy")
        data = np.load(file_path)
        rep_data.append(data)

    rep_data = np.vstack(rep_data)

    print(rep_data.shape)
    print(atom_order.shape)
    
    for atom, data_arr in zip(atom_order,rep_data):
        atom_to_file[atom].append(data_arr)

    for atom, v in atom_to_file.items():
        file_name = f"{atom}_{rep}.npy"
        np.save(file_name, np.array(v))   
     
print("Process completed successfully.")
