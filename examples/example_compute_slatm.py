#!/usr/bin/env python3

import os
import numpy as np
from qstack import compound
from qstack.qml import slatm

def compute_slatm(xyz_file, qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03):
    """Process a XYZ file to compute the (a)SLATM representation.

    Args:
        q (str): .
        r (list): .
        mbtypes (int): .
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
    mol = compound.xyz_to_mol(xyz_file, 'ccpvqz', charge=+1, spin=1)

    qs = [mol.numbers for mol in molecules]
    mbtypes = slatm.get_mbtypes([qs], qml=False)

    q = [mol.symbols for mol in molecules]
    r = [mol.atom_coords(unit='Bohr') for mol in molecules]
    X = slatm.get_slatm([q], [r], mbtypes, qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03)
    return X

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(path, 'data')
    results_dir = os.path.join(path, 'results')
    logs_file = os.path.join(path, 'list_of_molecules.txt')
    results_file = os.path.join(results_dir, 'slatm.npy')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    with open(logs_file, 'r') as f:
        xyz_files = [line.strip() + ".xyz" for line in f.readlines()]

    results = [] 

    for xyz_filename in xyz_files:  
        xyz_path = os.path.join(data_dir, xyz_filename)
        if os.path.exists(xyz_path):
            X = compute_slatm([q], [r], [mbtypes], qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03)
            results.append(X)
        else:
            print(f"File not found: {xyz_path}")

    np.save(results_file, np.array(results))  
    print(f"Results saved to {results_file}")

if __name__ == "__main__":
    main()
