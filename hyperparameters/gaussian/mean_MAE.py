#!/usr/bin/env python3

import numpy as np
import sys
import os

atoms = sys.argv[1]
reps = sys.argv[2]

training_size = []
results = []

data_value_1 = {}
data_value_2 = {}
data_value_3 = {}
data_value_4 = {}
data_value_5 = {}

for i in range(1, 6):
    file_path = f"results/gaussian_regression_{atoms}_{reps}_split_{i}.txt"
    lines = np.loadtxt(file_path)
    results.append(lines)

    value_1_column_2 = lines[0, 1]
    data_value_1[i] = value_1_column_2

    value_2_column_2 = lines[1, 1]
    data_value_2[i] = value_2_column_2

    value_3_column_2 = lines[2, 1]
    data_value_3[i] = value_3_column_2

    value_4_column_2 = lines[3, 1]
    data_value_4[i] = value_4_column_2

    value_5_column_2 = lines[4, 1]
    data_value_5[i] = value_5_column_2

    training_size_1 = lines[0, 0]
    training_size_2 = lines[1, 0]
    training_size_3 = lines[2, 0]
    training_size_4 = lines[3, 0]
    training_size_5 = lines[4, 0]

mean_value_1 = np.mean(list(data_value_1.values()))
mean_value_2 = np.mean(list(data_value_2.values()))
mean_value_3 = np.mean(list(data_value_3.values()))
mean_value_4 = np.mean(list(data_value_4.values()))
mean_value_5 = np.mean(list(data_value_5.values()))
std_value_1 = np.std(list(data_value_1.values()))
std_value_2 = np.std(list(data_value_2.values()))
std_value_3 = np.std(list(data_value_3.values()))
std_value_4 = np.std(list(data_value_4.values()))
std_value_5 = np.std(list(data_value_5.values()))

output_file = f"results/mean_MAE_{atoms}_{reps}.txt"
with open(output_file, "w") as f:
    f.write(f"{training_size_1} {mean_value_1:.18f} {std_value_1:.18f}\n")
    f.write(f"{training_size_2} {mean_value_2:.18f} {std_value_2:.18f}\n")
    f.write(f"{training_size_3} {mean_value_3:.18f} {std_value_3:.18f}\n")
    f.write(f"{training_size_4} {mean_value_4:.18f} {std_value_4:.18f}\n")
    f.write(f"{training_size_5} {mean_value_5:.18f} {std_value_5:.18f}\n")

print(f"Mean MAE and STD have been written to {output_file}")
~                                                                                                       
