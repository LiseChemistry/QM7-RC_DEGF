#!/usr/bin/env python3

import numpy as np

atoms = ["C", "H", "N", "S", "O"]
reps = ["a_slatm", "a_spahm", "b_spahm"]

for atom in atoms:
    for rep in reps:
        fichiers = [f"results/gaussian_regression_{atom}_{rep}_split_{i}.txt" for i in range(1, 6)]

        data = {}

        for fichier in fichiers:
            try:
                with open(fichier, "r") as f:
                    for ligne in f:
                        elements = ligne.strip().split()
                        if len(elements) < 2:
                            continue

                        cle = elements[0]
                        valeur = float(elements[1])

                        if cle not in data:
                            data[cle] = []
                        data[cle].append(valeur)
            except FileNotFoundError:
                print(f"File not found : {fichier}")
                continue

        output_file = f"mean_MAE_{atom}_{rep}.txt"
        with open(output_file, "w") as sortie:
            for cle, valeurs in data.items():
                moyenne = np.mean(valeurs)
                sortie.write(f"{cle} {moyenne:.2f}\n")

        print(f"Mean MAE in {output_file}")
