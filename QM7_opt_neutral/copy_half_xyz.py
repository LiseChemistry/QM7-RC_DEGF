#!/usr/bin/env python3

import os
import shutil

list_mol = '/home/student5/lise/MasterProject_SPAHM-ENN/good_logs_list.txt'
direction_input_neutral = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/1_QM7/xyz'
direction_input_cation = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_RC_optimized_xyz'
direction_output = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral_RC/'

with open(list_mol, 'r') as file:
    file_names = [name.strip() for name in file.readlines()[:3558]]

for file_name in file_names:
    full_file_name = f"{file_name}.xyz"

    file_path_non_opt = os.path.join(direction_input_neutral, full_file_name)
    file_path_opt = os.path.join(direction_input_cation, full_file_name)

    if os.path.isfile(file_path_opt):
        new_name = f"{file_name}_1.xyz"
        shutil.copy(file_path_opt, os.path.join(direction_output, new_name))
    else:
        print(f"No file : {file_path_opt}")

    if os.path.isfile(file_path_non_opt):
        new_name = f"{file_name}_0.xyz"
        shutil.copy(file_path_non_opt, os.path.join(direction_output, new_name))
    else:
        print(f"No file : {file_path_non_opt}")
