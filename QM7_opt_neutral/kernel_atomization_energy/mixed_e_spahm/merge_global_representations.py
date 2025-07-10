#!/usr/bin/env python3

import os
import numpy as np

results_directory = 'representations'
output_file = 'data_e_spahm.npy'
log_file = 'list_mixed_data.txt'

with open(log_file, 'r') as f:
    molecule_files = [line.strip() + '.npy' for line in f if line.strip()]

lines = []
lengths = []

for molecule_file in molecule_files:
    file_path = os.path.join(results_directory, molecule_file)

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                line = f.readline().strip()
                if line:
                    line = line.replace('[', '').replace(']', '')
                    arr = np.array(line.split(), dtype=float)
                    lines.append(arr)
                    lengths.append(len(arr))
        except Exception as e:
            print(f"Erreur avec {file_path} : {e}")
    else:
        print(f"Fichier non trouvé : {file_path}")

from collections import Counter
if lengths:
    common_length = Counter(lengths).most_common(1)[0][0]
    filtered_lines = [line for line in lines if len(line) == common_length]
    print(f"{len(filtered_lines)} vecteurs gardés (longueur = {common_length}) sur {len(lines)} totaux")
    lines_array = np.stack(filtered_lines)
else:
    lines_array = np.array([])

np.save(output_file, lines_array)

print(f"{len(lines_array)} lignes enregistrées dans {output_file}")
print("Contenu du tableau :\n", lines_array)
