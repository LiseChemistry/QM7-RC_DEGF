#!/usr/bin/env python3

import os
import shutil

source_dir = 'results'
target_dir = 'representations'

for filename in os.listdir(source_dir):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(target_dir, filename)
    shutil.copy(src, dst)

def complete_vector(vec, target_length=33):
    """
    Complete a vector in the form of a string with zeros until it reaches the target length.
    """
    if len(vec) < target_length:
        vec += ['0.0'] * (target_length - len(vec))  
    return vec

def process_file(file_path):
    """
    Process each file while keeping the data in the form of strings.
    """
    with open(file_path, 'r') as file:
        lines = file.read()

        lines = lines.replace('] [', '],[')

        data = []
        for line in lines.strip().split("\n"):
            vec = line.split()
            data.append(vec)

    vector1 = complete_vector(data[0])
    vector2 = complete_vector(data[1])

    with open(file_path, 'w') as f:
        f.write(" ".join(vector1) + "\n")
        f.write(" ".join(vector2) + "\n")

for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    process_file(file_path)

print("Finished.")

