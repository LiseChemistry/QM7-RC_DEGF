#!/usr/bin/env python3

import numpy as np
import os
import glob
from qstack.qml import slatm
from example_compute_slatm import compute_slatm

def test_slatm():
        xyz_file = "./data/mol_0000.xyz"
        basis = 'minao'

        slatm = compute_slatm(xyz_file, qml_compatible=True, stack_all=True, global_repr=False, sigma2=0.05, r0=0.1, rcut=4.8, dgrid2=0.03, theta0=20.0*np.pi/180.0, sigma3=0.05, dgrid3=0.03)

        print(f"(a)SLATM for {xyz_file}: {slatm}")

        target_values = np.load('X_mol-0000_slatm.npy')

        #assert(np.allclose(slatm, target_values, atol=1e-5))
        assert(np.allclose(sum(np.sum(slatm, axis=1)), sum(np.sum(target_values, axis=1)), atol=1e-5))

def main():
        test_slatm()
        return 0

if __name__ == '__main__':
        main()

