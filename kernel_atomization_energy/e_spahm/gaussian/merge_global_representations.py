#!/usr/bin/env python3

import os
import numpy as np

results_directory = 'glob_representations'
output_file = 'list_glob_representations.npy'
log_file = 'good_logs_list.txt'

with open(log_file, 'r') as f:
    molecule_files = [line.strip() + '.txt' for line in f if line.strip()]

lines = []

for molecule_file in molecule_files:
    file_path = os.path.join(results_directory, molecule_file)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            line = f.readline().strip()
            if line:  
                lines.append(np.array(line.split(), dtype=float))

lines_array = np.array(lines)
np.save(output_file, lines_array)

print(f"{len(lines)} lignes enregistrées dans {output_file}")
print("Contenu du tableau :\n", lines_array)
