#!/usr/bin/env python3

import os
import numpy as np
import shutil
import ast

source_dir = 'results'
target_dir = 'representations'

for filename in os.listdir(source_dir):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(target_dir, filename)
    shutil.copy(src, dst)

def complete_vector(vec, target_length=33):
    if len(vec) < target_length:
        vec += [0.0] * (target_length - len(vec))  
    return vec

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.read()
        lines = lines.replace('] [', '],[')

        data = []
        for line in lines.strip().split("\n"):
            vec = list(map(float, line.split()))
            data.append(vec)

    vector1 = complete_vector(data[0])
    vector2 = complete_vector(data[1])

    with open(file_path, 'w') as f:
        f.write(" ".join(map(str, vector1)) + "\n")
        f.write(" ".join(map(str, vector2)) + "\n")

for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    process_file(file_path)

print("Finished.")
