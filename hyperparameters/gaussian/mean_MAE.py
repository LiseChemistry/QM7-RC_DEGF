#!/usr/bin/env python3

import numpy as np
import sys
import os

atoms = sys.argv[1]
reps = sys.argv[2]
results_dir = "results"
data = {}

for i in range(1, 6):
    file_path = f"{results_dir}/gaussian_regression_{atoms}_{reps}_split_{i}.txt"

    with open(file_path, "r") as file:
        for ligne in file:
            elements = ligne.strip().split()
            training_size = elements[0]
            value = float(elements[1])

            if training_size not in data:
                data[training_size] = []

            data[training_size].append(value)

output_file = f"mean_MAE_{atoms}_{reps}.txt"
with open(output_file, "w") as sortie:
    for training_size, values in data.items():
        mean = np.mean(values)
        std = np.std(values)
        sortie.write(f"{training_size} {mean:.18f} {std:.18f}\n")

print(f"Mean MAE has been written to {output_file}")

~                                                                    
