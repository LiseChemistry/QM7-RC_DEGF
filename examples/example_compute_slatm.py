#!/usr/bin/env python3

import os
import numpy as np
from qstack.qml import slatm

logs_list_path = './list_of_molecules.txt'
xyzs_directory = './data'

results_directory = './'

with open(logs_list_path, 'r') as file:
    molecules = [line.strip() for line in file.readlines()]

np.set_printoptions(threshold=np.inf, linewidth=100)

for molecule in molecules:
    xyzs = os.path.join(xyzs_directory, f"{molecule}.xyz")

    if os.path.exists(xyzs):
        try:
            v = slatm.get_slatm_for_dataset([xyzs], progress=False)
            n, m = v.shape  

            output_file_path = os.path.join(results_directory, f"{molecule}.txt")

            with open(output_file_path, 'w') as output_file:
               
                output_file.write(f"array(\n{np.array2string(v, separator=', ', threshold=np.inf)}\n)\n")

            print(f"SLATM for {molecule}: {output_file_path}")

        except Exception as e:
            print(f"Error {molecule}: {e}")
    else:
        print(f"{xyzs} does not exist.")
