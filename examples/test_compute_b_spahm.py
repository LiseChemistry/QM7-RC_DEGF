#!/usr/bin/env python3

from qstack.spahm import compute_spahm
import numpy as np
import os
from qstack import compound, spahm
from example_compute_b_spahm import compute_b_spahm
from qstack.spahm.rho import bond

def test_b_spahm():
        xyz_file = "./data/mol_0000.xyz"
        logs_file =  "./list_of_molecules.txt"
       # basis = 'minao'

        b_spahm = compute_b_spahm(xyz_file, logs_file, guess="LB", spin=1, readdm=None, pairfile=None, dump_and_exit=False, same_basis=False, omods=["alpha", "beta"], elements=["H", "C", "N", "O", "S"], only_m0=False, zeros=False, split=False, printlevel=0, with_symbols=False, only_z=[], merge=True)

        print(f"(b)SPAHM for {xyz_file}: {b_spahm}")

        target_values = np.load('X_mol-0000_bond.npy')

        assert(np.allclose(b_spahm, target_values, atol=1e-5))

def main():
        test_b_spahm()
        return 0

if __name__ == '__main__':
        main()
