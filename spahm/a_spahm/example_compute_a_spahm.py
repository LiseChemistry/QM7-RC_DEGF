#!/usr/bin/env python3

import os
import sys
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
    mol = compound.xyz_to_mol(xyz_file, 'minao', charge=1, spin=1)

    X = atom.get_repr(mol, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"])
    X = np.array([x for x in X[:,1]])
    return X


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, './QM7_RC_optimized_xyz')
    results_dir = os.path.join(path, '/home/student5/lise/MasterProject_SPAHM-ENN/spahm/a_spahm/results')
    logs_file = os.path.join(path, 'good_logs_list.txt')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    xyz_path = sys.argv[1]

    if os.path.exists(xyz_path):
        X = compute_a_spahm(xyz_path, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"])
    else:
        print(f"File not found: {xyz_path}")

    results_file = os.path.join(results_dir, f"{os.path.splitext(os.path.basename(xyz_path))[0]}.npy")
    np.save(results_file, np.array(X))  
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()

