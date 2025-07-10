#!/usr/bin/env python3

# Lecture des fichiers d'energies
energies_0 = {}
with open('Atomization_energies_0.txt', 'r') as f0:
    for line in f0:
        parts = line.strip().split()
        if len(parts) == 2:
            molecule, energy = parts
            energies_0[molecule] = energy

energies_1 = {}
with open('Atomization_energies_1.txt', 'r') as f1:
    for line in f1:
        parts = line.strip().split()
        if len(parts) == 2:
            molecule, energy = parts
            energies_1[molecule] = energy

# Lecture de la liste melangee et ecriture des resultats
with open('list_mixed_data.txt', 'r') as f_list, open('Atomization_energy.txt', 'w') as fout:
    for line in f_list:
        mol = line.strip()
        if mol.endswith('_0'):
            energy = energies_0.get(mol, 'N/A')
        elif mol.endswith('_1') or mol.endswith('+1'):
            energy = energies_1.get(mol, 'N/A')
        else:
            energy = 'N/A'  # au cas ou il y aurait une erreur

        fout.write(f"{mol} {energy}\n")

