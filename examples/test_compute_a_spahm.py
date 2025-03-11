#!/usr/bin/env python3

from qstack.spahm import compute_spahm
import numpy as np
import os
from qstack import compound, spahm
from example_compute_a_spahm import compute_a_spahm
from qstack.spahm.rho import atom

def test_a_spahm():
        xyz_file = "./data/mol_0000.xyz"
        basis = 'minao'

        a_spahm = compute_a_spahm(xyz_file, elements=["H", "C", "N", "O", "S"], charge=+1, spin=1, dm=None, guess="LB", model="lowdin-long-x", only_z=None, open_mod=["alpha", "beta"])

        print(f"(a)SPAHM for {xyz_file}: {a_spahm}")

        target_values = np.array(np.load('X_mol-0000_atom.npy'))

        assert(np.allclose(a_spahm, target_values, atol=1e-5))

def main():
        test_a_spahm()
        return 0

if __name__ == '__main__':
        main()
