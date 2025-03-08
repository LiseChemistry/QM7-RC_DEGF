#!/usr/bin/env python3

from qstack.spahm import compute_spahm
import numpy as np
import os
from qstack import compound, spahm
from example_compute_a_spahm import compute_a_spahm
from qstack.spahm.rho import atom

def test_a_spahm():
        xyz_file = "./data/mol_0000.xyz"
        basis = 'ccpvqz'

        a_spahm = compute_a_spahm(xyz_file, basis, charge=+1, spin=1)

        print(f"(a)SPAHM for {xyz_file}: {a_spahm}")

        target_values = np.array([])

        assert(np.allclose(a_spahm, target_values, atol=1e-5))

def main():
        test_a_spahm()
        return 0

if __name__ == '__main__':
        main()
