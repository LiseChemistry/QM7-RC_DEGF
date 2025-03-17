#!/usr/bin/env python3

import sys
import os

atoms_file = 'list_atoms.txt'
charges_file = 'list_charges.txt'

output_files = {
    'C': 'C_charges.txt',
    'N': 'N_charges.txt',
    'O': 'O_charges.txt',
    'H': 'H_charges.txt',
    'S': 'S_charges.txt'
}

with open(atoms_file, 'r') as atoms, open(charges_file, 'r') as charges:
    atom_lines = atoms.readlines()
    charge_lines = charges.readlines()

if len(atom_lines) != len(charge_lines):
    print("Error: The files do not have the same number of lines.")
    sys.exit(1)

sorted_charges = {key: [] for key in output_files.keys()}

for atom, charge in zip(atom_lines, charge_lines):
    atom = atom.strip()
    charge = charge.strip()
    if atom in sorted_charges:
        sorted_charges[atom].append(charge)

for atom_type, filename in output_files.items():
    with open(filename, 'w') as f:
        f.write('\n'.join(sorted_charges[atom_type]) + '\n')

print("Sorting charges completed successfully.")
