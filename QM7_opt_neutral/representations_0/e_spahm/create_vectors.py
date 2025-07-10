#!/usr/bin/env python3

import os
import shutil
import re

source_dir = 'results'
target_dir = 'representations'

for filename in os.listdir(source_dir):
    src = os.path.join(source_dir, filename)
    dst = os.path.join(target_dir, filename)
    shutil.copy(src, dst)

def complete_vector(vec, target_length=33):
    """
    Completes a vector (list of strings) with '0.0' until it reaches the target_length.
    """
    if len(vec) < target_length:
        vec += ['0.0'] * (target_length - len(vec))
    return vec

def process_file(file_path):
    """
    Extracts the vectors between brackets and processes them.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    raw_vectors = re.findall(r'\[([^\]]+)\]', content)

    processed_lines = []
    for raw_vec in raw_vectors:
        raw_vec = raw_vec.lstrip('[')
        vec = raw_vec.strip().split()
        completed_vec = complete_vector(vec)
        processed_lines.append(" ".join(completed_vec))

    combined_lines = []
    for i in range(0, len(processed_lines), 2):
        if i + 1 < len(processed_lines):
            combined_lines.append([processed_lines[i], processed_lines[i + 1]]) 
        else:
            combined_lines.append([processed_lines[i]])

    final_lines = []
    for pair in combined_lines:
        final_lines.extend(pair)

    with open(file_path, 'w') as f:
        f.write(" ".join(final_lines) + "\n")

for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    process_file(file_path)

print("Finished.")
