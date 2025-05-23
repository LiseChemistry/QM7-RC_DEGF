#!/usr/bin/env python3

import os
import numpy as np

inputs = {
    'C': np.load('a_SLATM_C.npy'),
    'N': np.load('a_SLATM_N.npy'),
    'O': np.load('a_SLATM_O.npy'),
    'H': np.load('a_SLATM_H.npy'),
    'S': np.load('a_SLATM_S.npy')
}

indices = {atom: 0 for atom in inputs}

mol_data = {}

with open('list_atoms.txt') as f:
    for line in f:
        atom, mol = line.strip().split()

        if atom not in inputs:
            continue

        vec = inputs[atom][indices[atom]]
        indices[atom] += 1

        if mol not in mol_data:
            mol_data[mol] = []
        mol_data[mol].append(vec)

for mol, vectors in mol_data.items():
    np.save(f'glob_representations/{mol}.npy', np.stack(vectors))

print("File is saved in 'glob_representations/'")

