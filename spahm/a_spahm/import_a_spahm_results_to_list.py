#!/usr/bin/env python3

import numpy as np

with open('data_a_spahm.csv', 'w', encoding='utf-8') as f:
    with open('good_logs_list.txt') as f_list:
        for line in f_list:
            fname = 'results/' + line.strip() + '.npy'
            if fname:
                data = np.load(fname)
                summed = np.sum(data, axis=0, keepdims=True)

                f.write(' '.join(map(str, summed.flatten())) + '\n')
