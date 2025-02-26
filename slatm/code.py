#!/usr/bin/env python3

import os
import numpy as np
from qstack.qml import slatm

logs_list_path = '/home/student5/lise/MasterProject_SPAHM-ENN/logs_list.txt'
xyzs_directory = '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_RC_optimized_xyz'

results_directory = '/home/student5/lise/MasterProject_SPAHM-ENN/slatm'

with open(logs_list_path, 'r') as file:
    molecules = [line.strip() for line in file.readlines()]

for molecule in molecules:
    xyzs = os.path.join(xyzs_directory, f"{molecule}.xyz")  
    
    if os.path.exists(xyzs):
        try:
            v = slatm.get_slatm_for_dataset([xyzs], progress=False)

            output_file_path = os.path.join(results_directory, f"{molecule}.txt")

            with open(output_file_path, 'w') as output_file:
                output_file.write(f"array({np.array2string(v, separator=', ')})\n")
            
            print(f"SLATM calculé et sauvegardé pour {molecule}: {output_file_path}")
        
        except Exception as e:
            print(f"Erreur pour {molecule}: {e}")
    else:
        print(f"Le fichier {xyzs} n'existe pas.")


