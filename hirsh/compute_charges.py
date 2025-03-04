#!/usr/bin/env python3

import os
import numpy as np
from qstack import compound, fields
from qstack.fields.decomposition import decompose
from qstack.fields.hirshfeld import hirshfeld_charges, spherical_atoms

def compute_charges_for_mol():
    """ This function  does something
    TODO: complete the docs
    """

    return 0



def main():

    xyz_folder = "../QM7_RC_non_optimized_xyz/"
    output_folder = "/home/student/MasterProject_SPAHM-ENN/hirsh/"  ## change to relative paths
    logs_list = "/home/student/MasterProject_SPAHM-ENN/logs_list.txt"  ## change to relative paths
    
    with open(logs_list, "r") as f:
        file_list = [line.strip() for line in f.readlines()]
    ## The following should go in some funtion
    for file_name in file_list:
        xyz_file = os.path.join(xyz_folder, file_name + ".xyz")
    
        if not os.path.exists(xyz_file):
            print(f"File not found: {xyz_file} (Skipping)")
            continue
    
        print(f"File: {xyz_file}")
    
        mol = compound.xyz_to_mol(xyz_file, 'def2svp', charge=1, spin=1)
        atm_bas = 'def2svp'
        dm_atoms = spherical_atoms(set(mol.elements), atm_bas)
        dm = fields.dm.get_converged_dm(mol, xc="wB97XD")
    
        if dm.ndim == 3 and dm.shape[0] == 2:
            cd_total = dm[0] + dm[1]
        else:
            cd_total = dm
    
        print(f"Debug - dm shape: {dm.shape}")
    
        ho_dm = hirshfeld_charges(mol, cd_total, dm_atoms=dm_atoms, atm_bas=atm_bas, dominant=True, occupations=False, grid_level=3)
        auxmol, c = decompose(mol, cd_total, 'def2svp')
    
        if c.ndim == 3 and c.shape[0] == 2:
            c_total = c[0] + c[1]
        else:
            c_total = c
    
        ho_fit = hirshfeld_charges(auxmol, c_total, dm_atoms=dm_atoms, atm_bas=atm_bas, dominant=True, occupations=False, grid_level=3)

        ## The result should be returned by the function and saved using the main function
    
        output_file = os.path.join(output_folder, f"{file_name}.txt")
        with open(output_file, "w") as f:
            f.write(f"dm: {ho_dm}\n")
            f.write(f"fit: {ho_fit}\n")
    
        print(f"Results :{output_file}")

        return 0

if __name__ == "__main__":
    main()
