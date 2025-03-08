#!/usr/bin/env python3

import os
import numpy as np
from qstack import compound
from qstack.spahm import compute_spahm

def compute_e_spahm(xyz_file, basis, charge=1, spin=1):
    """Process a XYZ file to compute the (e)SPAHM representation.

    Args:
        xyz_file (str): Name (including path) of a XYZ file.
        basis (str or dict): Basis set.
        charge (int): Molecule's charge.
        spin (int): Molecule's spin (alpha electrons - beta electrons).

    Returns:
        np.ndarray: The SPAHM representation.
    """
    mol = compound.xyz_to_mol(xyz_file, basis, charge=charge, spin=spin)
    X = compute_spahm.get_spahm_representation(mol, "lb")
    return X

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, 'data')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'list_of_molecules.txt')
    results_file = os.path.join(results_dir, 'e_spahm.npy')
    basis = 'minao'

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    with open(logs_file, 'r') as f:
        xyz_files = [line.strip() + ".xyz" for line in f.readlines()]

    results = []
    for xyz_filename in xyz_files:
        xyz_path = os.path.join(data_dir, xyz_filename)
        if os.path.exists(xyz_path):
            X = compute_e_spahm(xyz_path, basis, charge=0, spin=0)  # Suppression des arguments non définis (ignore, unit, ecp)
            results.append(X)
        else:
            print(f"File not found: {xyz_path}")

    np.save(results_file, np.array(results))
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()

