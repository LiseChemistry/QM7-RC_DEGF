#!/usr/bin/env python3

import numpy as np
import os

atoms_file = 'list_atoms.txt'
log_list = '/home/student5/lise/MasterProject_SPAHM-ENN/good_logs_list.txt'
representations = ["a_spahm", "b_spahm", "charges"]
directories = {
    "a_spahm": "/home/student5/lise/MasterProject_SPAHM-ENN/spahm/a_spahm/results",
    "b_spahm": "/home/student5/lise/MasterProject_SPAHM-ENN/spahm/b_spahm/results",
    "charges": "/home/student5/lise/MasterProject_SPAHM-ENN/hirsh/results"
}
atoms_list = ['C', 'H', 'S', 'O', 'N']
atom_order = np.loadtxt(atoms_file, dtype=str)

with open(log_list, 'r', encoding='utf-8') as file:
    list_names = [line.strip() for line in file]

atom_to_file = {atom: [] for atom in atoms_list}

for rep in representations:
    rep_data = []

    for file_name in list_names:
        file_path = os.path.join(directories[rep], f"{file_name}.npy")
        data = np.load(file_path)
        rep_data.append(data)

    np.save(f"list_{rep}.npy", np.array(rep_data))

print(f"atom_order shape: {atom_order.shape}, length: {len(atom_order)}")
rep_data = np.array(rep_data)
print(f"rep_data shape: {rep_data.shape}, length: {len(rep_data)}")

if len(atom_order) == len(rep_data):
    print("Same.")
else:
    print("Not the same.")

rep_data = np.ndarray(shape=len(rep_data))

for atom,rep in zip(atom_order,rep_data):
    atom_to_file[atom].append(rep)
for k,v in atom_to_file.items():
    np.save(f"{k}_{rep}.npy", np.array(v))

print("Process completed successfully.")
