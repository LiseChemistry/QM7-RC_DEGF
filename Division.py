import os

input_file = '/home/student/Documents/QM7/structures.txt'
output_dir = '/home/student/Documents/QM7/molecules_xyz'

os.makedirs(output_dir, exist_ok=True)

with open(input_file, "r") as file:
    lines = file.readlines()

molecule_count = 0
i = 0
total_lines = len(lines)

while i < total_lines - 1:
    line = lines[i].strip()

    if line.isdigit() and i + 1 < total_lines and lines[i + 1].strip() == "":
        num_atoms = int(line)
        print(f"Molécule détectée avec {num_atoms} atomes à la ligne {i}")

        if i + 1 + num_atoms < total_lines:
            molecule_data = [line + "\n", "\n"] 
            molecule_data += lines[i + 2 : i + 2 + num_atoms] 

            filename = os.path.join(output_dir, f"mol{molecule_count:03d}.xyz")
            with open(filename, "w") as mol_file:
                mol_file.writelines(molecule_data)

            molecule_count += 1
            i += num_atoms + 1

    i += 1 

print(f"{molecule_count} molécules extraites et enregistrées dans {output_dir}/")