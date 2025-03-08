#!/usr/bin/env python3

import numpy as np
import os
from qstack import compound, fields
from qstack.fields.decomposition import decompose
from qstack.fields.hirshfeld import hirshfeld_charges,spherical_atoms
from test_compute_charges import process_xyz_file


def test_charges():
	xyz_file = "./data/mol_0000.xyz"
	atm_bas = 'ccpvqz'
	
	compute_charges = process_xyz_file(xyz_file, atm_bas, charge=1, spin=1)
	
	print(f"Computed Hirshfeld charges for {xyz_file}: {compute_charges}")
	
	target_values = np.array([-2.417224233767925057e-01, 3.089443963559630468e-01, 3.063794059082041166e-01, 3.127901061228439694e-01, 3.136076954580468978e-01])

	assert(np.allclose(compute_charges, target_values, atol=1e-5))
	
def main():
	test_charges()
	return 0

if __name__ == '__main__':
	main()
