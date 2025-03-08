#!/usr/bin/env python3

from qstack.spahm import compute_spahm
import numpy as np
import os
from qstack import compound, spahm
from example_compute_b_spahm import compute_b_spahm
from qstack.spahm.rho import bond

def test_b_spahm():
        xyz_file = "./data/mol_0000.xyz"
        basis = 'ccpvqz'

        b_spahm = compute_b_spahm(xyz_file, basis, charge=+1, spin=1)

        print(f"(b)SPAHM for {xyz_file}: {e_spahm}")

        target_values = np.array([])

        assert(np.allclose(b_spahm, target_values, atol=1e-5))

def main():
        test_b_spahm()
        return 0

if __name__ == '__main__':
        main()
