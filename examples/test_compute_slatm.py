#!/usr/bin/env python3

import numpy as np
import os
import glob
from qstack.qml import slatm
from example_compute_slatm import compute_slatm

def test_slatm():
        xyz_file = "./data/mol_0000.xyz"
        basis = 'ccpvqz'

        slatm = compute_slatm(xyz_file, basis, charge=+1, spin=1)

        print(f"(a)SLATM for {xyz_file}: {slatm}")

        target_values = np.array([])

        assert(np.allclose(slatm, target_values, atol=1e-5))

def main():
        test_slatm()
        return 0

if __name__ == '__main__':
        main()

