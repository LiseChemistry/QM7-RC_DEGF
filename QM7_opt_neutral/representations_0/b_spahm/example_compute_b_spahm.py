#!/usr/bin/env python3

import os
import sys
import numpy as np
from qstack import compound, spahm
from qstack.spahm.rho import bond

def compute_b_spahm(xyz_file, logs_file, guess="LB", spin=0, readdm=None, pairfile=None, dump_and_exit=False, same_basis=False, omods=["alpha", "beta"], elements=["H", "C", "N", "O", "S"], only_m0=False, zeros=False, split=False, printlevel=0, with_symbols=False, only_z=[], merge=True):
    """Process a XYZ file to compute the (b)SPAHM representation.

    Args:
        xyz_file (str): Name (including path) of a XYZ file.
        guess (str): Initial guess Hamiltonian.
        spin (int): Molecule's spin (alpha electrons - beta electrons).
        readdm (str): path to the .npy file containins density matrices.
        pairfile (str): path to the pairfile (if None, atom pairs are detected automatically).
        dump_and_exit (bool): to save pairfile for the set of molecules (without generating representaitons).
        same_basis (bool): to use the same bond-optimized basis function for all atomic pairs (ZZ.bas == CC.bas for any Z).
        omods (list of str): Models for open-shell systems.
        elements (list): List of atomic elements.
        only_m0 (bool): use only basis functions with `m=0`.
        zeros (bool): add zeros features for non-existing bond pairs.
        split (bool): to split the final array into molecules.
        printlevel (int): level of verbosity.
        with_symbols (bool): to associate atomic symbol to representations in final array.
        only_z (str): List of selected atomic elements to specify the representation.
        merge (bool): to concatenate alpha and beta representations to a single feature vector.

    Returns:
        np.ndarray: The (b)SPAHM representation.
    """
    mol = compound.xyz_to_mol(xyz_file, 'minao', charge=0, spin=0)
    print(mol.charge)

    X = bond.get_repr([mol], logs_file, guess="LB", spin=[0], readdm=None, pairfile=None, dump_and_exit=False, same_basis=False, omods=["alpha", "beta"], elements=["H", "C", "N", "O", "S"], only_m0=False, zeros=False, split=False, printlevel=0, with_symbols=False, only_z=[], merge=True)
    return X

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, '/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/opt_neutral_xyz/xyz_opt_0_1/')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'list_all_neutral.txt')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    xyz_path = sys.argv[1]

    if os.path.exists(xyz_path):
        X = compute_b_spahm(xyz_path, logs_file, guess="LB", spin=0, readdm=None, pairfile=None, dump_and_exit=False, same_basis=False, omods=["alpha", "beta"], elements=["H", "C", "N", "O", "S"], only_m0=False, zeros=False, split=False, printlevel=0, with_symbols=False, only_z=[], merge=True)
    else:
        print(f"File not found: {xyz_path}")

    results_file = os.path.join(results_dir, f"{os.path.splitext(os.path.basename(xyz_path))[0]}.npy")
    np.save(results_file, np.array(X))
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()
