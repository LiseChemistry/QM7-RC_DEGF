#!/usr/bin/env python3

import numpy as np
import os

results_directory = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/mixed_data/e_spahm_mixed_data'
log_file = 'list_mixed_data.txt'

max_dim = 0
max_molecule_file = ""

with open(log_file, 'r') as f:
    molecule_files = f.read().splitlines()

for molecule_file in molecule_files:
    if not molecule_file.endswith('.npy'):
        molecule_file += '.npy'
    file_path = os.path.join(results_directory, molecule_file)

    arr = None
    try:
        arr = np.load(file_path, allow_pickle=True)
    except Exception as e_load:
        try:
            with open(file_path, 'r') as file:
                txt = file.read().replace('[', '').replace(']', '')
                arr = np.fromstring(txt, sep=' ')
        except Exception as e_text:
            print(f"Error processing {molecule_file}: {e_text}")
            continue

    if arr is not None:
        arr_shape = arr.shape
        if max(arr_shape) > max_dim:
            max_dim = max(arr_shape)
            max_molecule_file = molecule_file

        print(f"Processing file: {molecule_file}")
        print(f"Array shape: {arr_shape}")

print(f"\nBiggest dimension: {max_dim}, from file: {max_molecule_file}")
