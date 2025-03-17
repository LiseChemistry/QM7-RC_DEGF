#!/usr/bin/env python3

import os

directory = '/home/student5/lise/MasterProject_SPAHM-ENN/hirsh/QM7_RC_optimized_xyz'

with open('good_logs_list.txt', 'r') as file:
    file_names = file.readlines()

file_names = [name.strip() for name in file_names]

print(f"List of molecules: {file_names}")

with open('list_atoms.txt', 'w') as list_file:
    for file_name in file_names:
        full_file_name = f"{file_name}.xyz"
        file_path = os.path.join(directory, full_file_name)

        print(f"Check the files: {full_file_name}")

        if os.path.exists(file_path):
            print(f"File {full_file_name} exists, loading the data...")

            with open(file_path, 'r') as xyz_file:
                xyz_file.readline()
                xyz_file.readline()

                for line in xyz_file:
                    parts = line.split()
                    if len(parts) > 0:
                        atom_type = parts[0]  
                        list_file.write(f"{atom_type}\n")

        else:
            print(f"File {full_file_name} was not found in {directory}")

print("Process finished.")

