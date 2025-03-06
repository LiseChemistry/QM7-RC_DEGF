#!/usr/bin/env python3

import numpy as np
import os
from qstack import compound, fields
from qstack.fields.decomposition import decompose
from qstack.fields.hirshfeld import hirshfeld_charges, spherical_atoms

def process_xyz_file(xyz_file, atm_bas, charge=1, spin=1):

    """For a XYZ file : 

        xyz_file : XYZ file of molecule
        atm_bas : basis set to use
        charge : charge of molecules
        spin : spin of molecules"""

    mol = compound.xyz_to_mol(xyz_file, atm_bas, charge=charge, spin=spin)

    """To calculate DM for spherical atoms from mol.elements and compute Hirshfeld charges

        mol.elements : list of elements
        mol : object which contains the information about a molecule
        xc : functional to compute xc
        dm : density matrix
        dm_atoms : atomic density matrix
        atm_bas : atomic basis set
        dominant : Boolean indicating whether to use the dominant partition for Hirshfeld weights
        occupations : To return the atomic occupations
        grid level : grid's level for numerical integrations"""

    dm_atoms = spherical_atoms(set(mol.elements), atm_bas)
    dm = fields.dm.get_converged_dm(mol, xc="pbe0")
    dm = dm[0] + dm[1]
    ho = hirshfeld_charges(mol, dm, dm_atoms=dm_atoms, atm_bas=atm_bas, dominant=True, occupations=False, grid_level=3)
    return ho

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, 'data')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'list_of_molecules.txt')
    results_file = os.path.join(results_dir, 'hirsh_charges.txt')
    atm_bas = 'ccpvqz'
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    with open(logs_file, 'r') as f:
        xyz_files = [line.strip() + ".xyz" for line in f.readlines()]
    
    with open(results_file, 'w') as f_out:
        for xyz_filename in xyz_files:
            xyz_path = os.path.join(data_dir, xyz_filename)
            if os.path.exists(xyz_path):
                ho = process_xyz_file(xyz_path, atm_bas)
                f_out.write(f'{ho}\n')
            else:
                print(f"File not found: {xyz_path}")
                
if __name__ == "__main__":
    main()

