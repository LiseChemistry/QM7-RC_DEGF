#!/usr/bin/env python3

import numpy as np
import os

directory = '/home/student5/lise/MasterProject_SPAHM-ENN/hirsh/results'

with open('good_logs_list.txt', 'r') as file:
    file_names = [line.strip() for line in file.readlines()]

print(f"List of molecules : {file_names}")

with open('list_charges.txt', 'w') as list_file:
    for file_name in file_names:
        full_file_name = f"{file_name}.npy"
        file_path = os.path.join(directory, full_file_name)

        print(f"Check the files : {full_file_name}")

        if os.path.exists(file_path):
            print(f"File {full_file_name} existes, loading the data...")
            data = np.load(file_path)
            for value in data:
                list_file.write(f"{value}\n")
        else:
            print(f"File {full_file_name} was not found in {directory}")

print("Procces finished.")
