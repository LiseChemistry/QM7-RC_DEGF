#!/usr/bin/env python3

import os
import shutil

list_mol = 'list_RC.txt'
direction_input = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_RC_optimized_log'
direction_output = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/opt_neutral_xyz/log_opt_0_1'

with open(list_mol, 'r') as file:
    file_names = [name.strip() for name in file.readlines()]

for file_name in file_names:
    file_path_opt = os.path.join(direction_input, f"{file_name}.log")

    if os.path.isfile(file_path_opt):
        shutil.copy(file_path_opt, os.path.join(direction_output, f"{file_name}_1.log"))
    else:
        print(f"No file: {file_path_opt}")
