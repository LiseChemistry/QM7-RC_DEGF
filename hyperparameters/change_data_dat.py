#!/usr/bin/env python3

import sys
import numpy as np

hyper_file = sys.argv[1]

hypers = np.loadtxt(hyper_file)

etas = set(hypers[:,3])
eta_dict = {str(e) : [] for e in etas}

for x in hypers:
    ref = x[3]
    eta_dict[str(x[3])].append(x)

for e, v in eta_dict.items():
    xarr = np.array(v)
    idsort = np.argsort(xarr[:,2])
    eta_dict[e] = xarr[idsort]

outname = hyper_file.split(".")[0]+".dat"

with open(outname, "w+") as fout:
    for e in etas:
        k = str(e)
        #fout.write(np.array_str(eta_dict[k])+"\n")
        np.savetxt(fout, eta_dict[k])
        fout.write("\n")
print("Finished writing")
