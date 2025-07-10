#!/usr/bin/env python3

import os
import shutil

list_mol = 'list_neutral.txt'
direction_input = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/representations_0/e_spahm/results'
direction_output = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/mixed_data/e_spahm_mixed_data'

with open(list_mol, 'r') as file:
    file_names = [name.strip() for name in file.readlines()]

for file_name in file_names:
    full_file_name = f"{file_name}.xyz"

    file_path_non_opt = os.path.join(direction_input, full_file_name)

    if os.path.isfile(file_path_opt):
        new_name = f"{file_name}.xyz"
        shutil.copy(file_path_opt, os.path.join(direction_output, new_name))
    else:
        print(f"No file : {file_path_opt}")
