#!/usr/bin/env python3

import os
import shutil

# Chemins
list_mol = 'good_logs_list.txt'
direction_input_non_opt = 'QM7_RC_non_optimized_xyz'
direction_input_opt = 'QM7_RC_optimized_xyz'
direction_output = 'QM7_opt_and_non_opt_xyz'

with open(list_mol, 'r') as file:
    file_names = [name.strip() for name in file.readlines()[:3558]]

for file_name in file_names:
    full_file_name = f"{file_name}.xyz"

    file_path_non_opt = os.path.join(direction_input_non_opt, full_file_name)
    file_path_opt = os.path.join(direction_input_opt, full_file_name)

    if os.path.isfile(file_path_opt):
        new_name = f"mol_{file_name}_opt.xyz"
        shutil.copy(file_path_opt, os.path.join(direction_output, new_name))
    else:
        print(f"No file : {file_path_opt}")

    if os.path.isfile(file_path_non_opt):
        new_name = f"mol_{file_name}_non_opt.xyz"
        shutil.copy(file_path_non_opt, os.path.join(direction_output, new_name))
    else:
        print(f"No file : {file_path_non_opt}")
