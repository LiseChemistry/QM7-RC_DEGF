#!/usr/bin/env python3

import os
import glob
from qstack import compound
from qstack.spahm import compute_spahm

xyz_folder = "/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/opt_neutral_xyz/xyz_opt_0_1"
output_folder = "./results"
mol_list_file = "list_all_neutral.txt"

with open(mol_list_file, "r") as f:
    mol_list = [line.strip() for line in f.readlines() if line.strip()]

print(f"Number of molecules to process: {len(mol_list)}")

for mol_name in mol_list:
    xyz_file = os.path.join(xyz_folder, f"{mol_name}.xyz")  

    if not os.path.exists(xyz_file):
        print(f"File not found: {xyz_file} (Skipping)")
        continue

    print(f"Processing: {xyz_file}")

    try:
        mol = compound.xyz_to_mol(xyz_file, 'def2svp', charge=0, spin=0)
        X = compute_spahm.get_spahm_representation(mol, "lb")
        output_file = os.path.join(output_folder, f"{mol_name}.npy")
        with open(output_file, "w") as f:
            f.write(f"{X}\n")

        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error processing {xyz_file}: {e}")
