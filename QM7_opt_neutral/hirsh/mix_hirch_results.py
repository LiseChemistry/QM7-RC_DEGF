#!/usr/bin/env python3

import os

source_dir = "/home/student5/lise/MasterProject_SPAHM-ENN/hirsh/results"
dest_dir = "/home/student5/lise/MasterProject_SPAHM-ENN/QM7_opt_neutral/hirsh/results"
list_file = "list_RC.txt"

with open(list_file, "r") as f:
    filenames = [line.strip() + ".npy" for line in f if line.strip()]

for filename in filenames:
    src_path = os.path.join(source_dir, filename)
    base, ext = os.path.splitext(filename)
    new_filename = base + "_1" + ext
    dest_path = os.path.join(dest_dir, new_filename)

    if os.path.exists(src_path):
        with open(src_path, "rb") as src_file:
            data = src_file.read()
        with open(dest_path, "wb") as dest_file:
            dest_file.write(data)
        print(f"Copied : from {filename} to {new_filename}")
    else:
        print(f"File not found : {src_path}")
