#!/usr/bin/env python3

import numpy as np
import os

results_directory = 'results/'
log_file = 'good_logs_list.txt'

max_dim = 0
max_molecule_file = ""

with open(log_file, 'r') as f:
    molecule_files = f.read().splitlines()

for molecule_file in molecule_files:
    if not molecule_file.endswith('.txt'):
        molecule_file += '.txt'
    file_path = os.path.join(results_directory, molecule_file)

    with open(file_path, 'r') as file:
        txt = file.read().replace('[', '').replace(']', '')
        arr = np.fromstring(txt, sep=' ')

        if max(arr.shape) > max_dim:
            max_dim = max(arr.shape)
            max_molecule_file = molecule_file

        print(f"Processing file: {molecule_file}")
        print(f"Array shape: {arr.shape}")
        
print(f"Biggest {max_dim}, for : {max_molecule_file}")
