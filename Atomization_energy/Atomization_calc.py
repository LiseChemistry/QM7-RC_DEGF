#!/usr/bin/env python3

import os
import numpy as np
import qstack as qs

outputfile = "/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/Atomization_energies.txt"
ZPEfile = "ZPE.txt"
E0_file = "E_0.txt"
mol_list = "mol_list.txt"
E_CNOSH_file = "E_CNOSH.txt"

E0_elements = {}
if os.path.exists(E_CNOSH_file):
    with open(E_CNOSH_file, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                element, energy = parts
                E0_elements[element] = float(energy)
else:
    print(f"Le fichier {E_CNOSH_file} est introuvable. Assurez-vous qu'il existe.")

print("Dictionnaire des énergies des atomes (élément : énergie):", E0_elements)

def get_zpe(index):
    with open(ZPEfile, 'r') as f:
        zpe_lines = f.readlines()
    return float(zpe_lines[index].strip())

def get_e0(index):
    with open(E0_file, 'r') as f:
        e0_lines = f.readlines()
    return float(e0_lines[index].strip())

def calculate_x_energies(molname):
    mol_path = f"/home/student5/lise/MasterProject_SPAHM-ENN/geom_optimized_xyz/{molname}.xyz"

    if not os.path.exists(mol_path):
        print(f"Fichier {mol_path} introuvable. Ignoré.")
        return 0.0

    mol = qs.compound.xyz_to_mol(mol_path, basis='Def2SVP', charge=1, spin=1, ignore=False, unit='ANG', ecp=None)
    mol_elements = mol.elements
    energy_sum = sum(E0_elements.get(element, 0) for element in mol_elements)
    return energy_sum

def calculate_atomization_energy(molname, index):
    mol_energy = calculate_x_energies(molname)
    zpe = get_zpe(index)
    e0 = get_e0(index)
    atomization_energy = mol_energy - zpe - e0
    return atomization_energy

with open(mol_list, 'r') as f:
    molnames = [line.strip() for line in f.readlines()]

resultats = []
for index, molname in enumerate(molnames):
    atomization_energy = calculate_atomization_energy(molname, index)
    print(f"Calcul de l'énergie d'atomisation pour {molname}: {atomization_energy}")
    resultats.append([molname, atomization_energy])

np.savetxt(outputfile, resultats, fmt="%s", delimiter="\t", header="Molecule\tAtomization_Energy (kcal/mol)", comments='')

print(f"Les énergies d'atomisation ont été sauvegardées dans {outputfile}")
