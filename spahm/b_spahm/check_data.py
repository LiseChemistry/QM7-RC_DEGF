#!/usr/bin/env python3

import numpy as np
import os

directory = '/home/student5/lise/MasterProject_SPAHM-ENN/spahm/b_spahm/results'

expected_second_dim = 2656

for filename in os.listdir(directory):
    if filename.endswith(".npy"):
        file_path = os.path.join(directory, filename)

        data = np.load(file_path)

        if data.shape[1] != expected_second_dim:
            print(f"File: {filename}")
            print(f"Shape: {data.shape}")
            print(f"Warning: The second dimension is {data.shape[1]}, but expected {expected_second_dim}")
            print("-" * 50)

print("Shape consistency check completed.")
