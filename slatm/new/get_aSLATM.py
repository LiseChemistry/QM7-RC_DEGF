#!/usr/bin/env python3
import os
import numpy as np
import argparse
from tqdm import tqdm
from qstack.qml import slatm
import qstack.compound as compound

parser = argparse.ArgumentParser(description='This script produces aSLATM representations for molecules in a given directory.')
parser.add_argument('--list', required=True, type=str, dest='list', help='a txt-file with the list of paths to geometries')
args = parser.parse_args()

def main():
    print("Loading mols:")
    pathlist = np.loadtxt(args.list, dtype=str)
    molecules = [compound.xyz_to_mol(f) for f in tqdm(pathlist)]
    nuclear_charges   = [mol.atom_charges() for mol in molecules]
    mbtypes   = slatm.get_mbtypes(nuclear_charges)

    reps = []
    for mol in tqdm(molecules):
        reps.append(slatm.get_slatm(mol.atom_charges(), mol.atom_coords(), mbtypes))

    elements = set(np.hstack([np.array(mol.elements) for mol in molecules]))
    a_slatm  = dict()
    for q in elements :
        a_slatm[q] = []
    for mol, r in zip(molecules, reps) :
        for q,v in zip(mol.elements, r) :
            a_slatm[q].append(v)

    for q in a_slatm :
        np.save(f'a_SLATM_{q}', a_slatm[q])

if __name__ == '__main__':
    main()
