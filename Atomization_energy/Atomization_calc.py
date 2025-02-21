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
geom_opt_xyz = "/home/student5/lise/MasterProject_SPAHM-ENN/geom_optimized_xyz/${molname}.xyz"

data = np.loadtxt(outputfile, dtype=str) ### create a dictionnary {Z  : E0}
elements = data[:, 0]  
energies = data[:, 1].astype(float)  
E0_elements = dict(zip(elements, energies))
print(E0_elements)

### use qstack to convert xyz to Mole to calcule the number of elements qstack.compound.xyz_to_mol()

def calculate_x_energies(molname):
    mol = qs.compound.xyz_to_mol(f"/home/student5/lise/MasterProject_SPAHM-ENN/geom_optimized_xyz/{molname}.xyz",
                                 basis='Def2SVP', charge=1, spin=2, ignore=False, unit='ANG', ecp=None)
    mol_elements = mol.elements  
    energy_sum = 0.0
    for element in mol_elements:
        energy_sum += E0_elements.get(element, 0) 
    return energy_sum

np.savetxt('', namelist)

### create a function to calculate an atomization energy for only one molecule
### use a dictionnary E0_elements energie --> sum+=dict(e) with energies in mol.elements
### calculate an atomization energy and return

resultats = [] ###create a list of results
for fichier in glob.glob(os.path.join(dossier_mol, "*.inp")):

    atomes = compter_atomes_pyscf(fichier)
    energie_totale = sum(atomes[element] * energies_atomiques.get(element, 0) for element in atomes)
    resultats.append('{}: mol_001 = {}\n'.format(fichier, energie_totale))

return

with open(outputfile, "w") as f:
    f.writelines(resultats)

print(outputfile)
                                                                                                                                                   60,17         Bot
def calculate_atomization_energy(molname):
    mol = qs.compound.xyz_to_mol(f"/home/student5/lise/MasterProject_SPAHM-ENN/geom_optimized_xyz/{molname}.xyz", 
                                 basis='Def2SVP', charge=1, spin=2, ignore=False, unit='ANG', ecp=None)
    mol_elements = mol.elements  
    energy_sum = 0.0
    for element in mol_elements:
        energy_sum += E0_elements.get(element, 0)  
    return energy_sum
resultats = []  
dossier_mol = "/home/student5/lise/MasterProject_SPAHM-ENN"
for fichier in glob.glob(os.path.join(dossier_mol, "*.inp")):
    molname = os.path.basename(fichier).replace(".inp", "") 
    energie_totale = calculate_atomization_energy(molname)
    resultats.append(f'{molname}: Atomization energy = {energie_totale:.8f} kcal/mol\n')
with open(outputfile, "w") as f:
    f.writelines(resultats)








    


























































