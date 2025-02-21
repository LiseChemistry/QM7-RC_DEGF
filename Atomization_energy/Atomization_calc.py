#!/usr/bin/env python3

import glob
import os
import re
import numpy as np
import qstack as qs

logfile = "/home/student5/lise/MasterProject_SPAHM-ENN/opt/${molname}/${molname}.log"
outputfile = "/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/Atomization_energies.txt"
ZPEfile = "ZPE.txt"
E0_file = "E_0.txt"
mol_list = "mol_list.txt"

E0_elements = {} ### create a dictionnary {Z  : E0}
with open(outputfile, "r") as f:
	np.loadtxt('/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/Atomization_energies.txt', usecols=1, dtype=str) > var1
	np.loadtxt('/home/student5/lise/MasterProject_SPAHM-ENN/Atomization_energy/Atomization_energies.txt', usecols=2) > var2

data = np.loadtxt(outputfile, dtype=str) ### create a dictionnary {Z  : E0}
elements = data[:, 0] 
energies = data[:, 1].astype(float) 
E0_elements = dict(zip(elements, energies))
print(E0_elements)

### ru sur  toutes les molecules

export str=$(mkdir ${molname}.xyz) -> utilise qstack pour creer Mol !!! utiliser qstack.compound.xyz_to_mol()

### mol.elements = tous les atom types dans la molecules 

np.savetxt('', namelist)

def compter_atomes_pyscf(fichier):
	mol = gto.Mole()
	mol.atom = open(fichier).read() 
	print("Mol.atom content:\n", mol.atom)
	mol.build()
	compteur = {"C": 0, "H": 0, "O": 0, "N": 0, "S": 0}
for symbole in mol.atom_symbol_list():
	if symbole in compteur:
	compteur[symbole] += 1
return compteur

### create a function to calculate an atomization energy for only one molecule
### use a dictionnary E0_elements energie --> sum+=dict(e) with energies in mol.elements
### calculate an atomization energy and return

resultats = [] ###create a list of results

for fichier in glob.glob(os.path.join(dossier_mol, "*.inp")):
    atomes = compter_atomes_pyscf(fichier)
    energie_totale = sum(atomes[element] * energies_atomiques.get(element, 0) for element in atomes)
    resultats.append('{}: mol_001 = {}\n'.format(fichier, energie_totale)) 

with open(outputfile, "w") as f:
    f.writelines(resultats)

print(outputfile)
