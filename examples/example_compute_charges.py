#!/usr/bin/env python3

import numpy as np
import os
from qstack import compound, fields
from qstack.fields.decomposition import decompose
from qstack.fields.hirshfeld import hirshfeld_charges, spherical_atoms

def process_xyz_file(xyz_file, atm_bas, charge=1, spin=1):
    """Process a XYZ file:

        Args:
            xyz_file : XYZ file of molecules
            atm_bas : basis set to use
            charge : charge of molecules
            spin : spin of molecules

        Returns:
            Computed Hirshfeld charge
         """

    mol = compound.xyz_to_mol(xyz_file, atm_bas, charge=charge, spin=spin)

    dm_atoms = spherical_atoms(set(mol.elements), atm_bas) # mol.elements : list of elements; atm_bas : atomic basis set
    dm = fields.dm.get_converged_dm(mol, xc="pbe0")  # mol:object which contains the information about a molecule; xc : functional to compute xc
    dm = dm[0] + dm[1] # dm : density matrix
    ho = hirshfeld_charges(mol, dm, dm_atoms=dm_atoms, atm_bas=atm_bas, dominant=True, occupations=False, grid_level=3) # dm_atoms : atomic density matrix; dominant : Boolean indicating whether to use the dominant partition for Hirshfeld weights; occupations : To return the atomic occupations; grid level : grid's level for numerical integrations
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
                ho = process_xyz_file(xyz_path, atm_bas, charge=1, spin=1)
                f_out.write(f'{ho}\n')
            else:
                print(f"File not found: {xyz_path}")

if __name__ == "__main__":
    main()
