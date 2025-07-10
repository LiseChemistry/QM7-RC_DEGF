#!/usr/bin/env python3

import numpy as np
import os

atoms_file = 'list_atoms.txt'
log_list = '/home/student5/lise/MasterProject_SPAHM-ENN/good_logs_list.txt'
representations = ["b_spahm", "a_spahm"]
directories = {
    "a_spahm": "/home/student5/lise/MasterProject_SPAHM-ENN/spahm/a_spahm/results",
    "b_spahm": "/home/student5/lise/MasterProject_SPAHM-ENN/spahm/b_spahm/results",
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
    
    for atom,rep in zip(atom_order,rep_data):
        atom_to_file[atom].append(rep)
    for atom,v in atom_to_file.items():
        file_name = f"{atom}_{rep}.npy"
        np.save(file_name, np.array(v))        
print("Process completed successfully.")
