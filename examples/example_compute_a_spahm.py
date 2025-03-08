#!/usr/bin/env python3

import os
import numpy as np
from qstack import compound, spahm
from qstack.spahm.rho import atom

def compute_a_spahm(xyz_file, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"]):
    """Process a XYZ file to compute the (a)SPAHM representation.

    Args:
        xyz_file (str): Name (including path) of a XYZ file.
        elements (list): List of atomic elements.
        charge (int): Molecule's charge.
        spin (int): Molecule's spin (alpha electrons - beta electrons).
        dm (str): Density matrix to load instead of computing the guess.
        guess (str): Initial guess Hamiltonian. 
        model (str): Model to create the representation.
        only_z (str): List of selected atomic elements to specify the representation.
        open_mod (): Model(s) for open-shell systems.

    Returns:
        np.ndarray: The (a)SPAHM representation.
    """
    mol = compound.xyz_to_mol(xyz_file, 'ccpvqz', charge=charge, spin=spin)

    X = atom.get_repr(mol, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"])
    return X

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, 'data')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'list_of_molecules.txt')
    results_file = os.path.join(results_dir, 'a_spahm.npy')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    with open(logs_file, 'r') as f:
        xyz_files = [line.strip() + ".xyz" for line in f.readlines()]

    results = []  

    for xyz_filename in xyz_files: 
        xyz_path = os.path.join(data_dir, xyz_filename)
        if os.path.exists(xyz_path):
            X = compute_a_spahm(xyz_path, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"])
            results.append(X)
        else:
            print(f"File not found: {xyz_path}")

    np.save(results_file, np.array(results))  
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()

