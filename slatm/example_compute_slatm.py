#!/usr/bin/env python3

import sys
import os
import numpy as np
import pyscf
from qstack import compound
from qstack.qml import slatm

def compute_slatm(xyz_file, qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03):
    """Process a XYZ file to compute the (a)SLATM representation.

    Args:
        xyz_file (str): path to a XYZ file.
        qml_compatible (bool): if False, the local representation (global_repr=False) is condensed.
        stack_all (bool): if stack the representations into one big ndarray.
        global_repr (bool): Return molecular SLATM if True, return atomic SLATM if False. 
        r0 (float): Grid range parameter (Å) [r0, rcut] for the 2-body term.
        rcut (float): Radial cutoff (Å) for the 2- and 3-body terms.
        sigma2 (float): Gaussian width for the 2-body term (Å).
        dgrid2 (float) : Grid spacing for the 2-body term (Å). 
        theta0 (float) : Grid range parameter (°) [theta0, 180-theta0] for the 3-body term.
        sigma3 (float) : Gaussian width for the 3-body term (°).
        dgrid3 (float) : Grid spacing for the 3-body term (°).

    Returns:
        np.ndarray: The (a)SLATM representation.
    """
    mol = compound.xyz_to_mol(xyz_file, 'minao', charge=+1, spin=1)
    qs = np.asarray([mol.atom_charge(i) for i in range(mol.natm)])
    print("Atomic numbers:", qs)
    qs_elements = [pyscf.gto.charge(z) for z in ["H", "C", "N", "O", "S"]]
    print(qs_elements)
    mbtypes = slatm.get_mbtypes([qs_elements], qml=False)
    print("mbtypes:", mbtypes)

    r = np.asarray([mol.atom_coord(i) for i in range(mol.natm)])
    print("Coordinates:\n", r)

    X = slatm.get_slatm(qs, r, mbtypes, qml_compatible=False, stack_all=True)
    return X

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, 'QM7_RC_optimized_xyz')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'good_logs_list.txt')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    xyz_path = sys.argv[1]

    if os.path.exists(xyz_path):
        X = compute_slatm(xyz_path, qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03)
    else:
        print(f"File not found: {xyz_path}")

    results_file = os.path.join(results_dir, f"{os.path.splitext(os.path.basename(xyz_path))[0]}.npy")
    np.save(results_file, np.array(X))
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()
