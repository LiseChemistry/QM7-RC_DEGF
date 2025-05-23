#!/usr/bin/env python3

import numpy as np

summed_data_list = []

with open('good_logs_list.txt') as f_list:
    for line in f_list:
        fname = 'glob_representations/' + line.strip() + '.npy'
        if fname:
            data = np.load(fname)
            summed = np.sum(data, axis=0, keepdims=True)
            summed_data_list.append(summed)

all_summed = np.vstack(summed_data_list)
np.save('data_slatm.npy', all_summed)
