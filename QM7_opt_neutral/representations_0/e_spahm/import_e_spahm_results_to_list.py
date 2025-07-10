#!/usr/bin/env python3

import numpy as np

with open('data_e_spahm.csv', 'w', encoding='utf-8') as f_out:
    with open('good_logs_list.txt', 'r', encoding='utf-8') as f_list:
        for line in f_list:
            fname = 'results/' + line.strip() + '.npy'
            data = np.load(fname)
            f_out.write(' '.join(map(str, data.flatten())) + '\n')
