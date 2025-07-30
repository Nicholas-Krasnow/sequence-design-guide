from pymol import cmd
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calculate_rmsd(pdb_file1, pdb_file2):
    cmd.reinitialize()
    cmd.load(pdb_file1, 'F1')
    cmd.load(pdb_file2, 'F2')
    alignment_result = cmd.super('F1', 'F2')
    rmsd = round(alignment_result[0], 4)
    cmd.delete('F1')
    cmd.delete('F2')
    return rmsd

pdb_ref = 'F_AF.pdb' #replace with the name of your pdb reference

structures = []

import re
directory = 'pdbs_rank001'
def extract_number_before_underscore(filename):
    match = re.match(r'(\d+)_', filename)
    return int(match.group(1)) if match else -1  # Use -1 to push non-matching files to the start

files = [
    f for f in os.listdir(directory)
    if os.path.isfile(os.path.join(directory, f)) and re.match(r'\d+_', f)
]

sorted_files = sorted(files, key=extract_number_before_underscore)

for x in sorted_files:
  structures.append('pdbs_rank001'+'/'+x)

vals = []
for x in structures:
   vals.append(calculate_rmsd(pdb_ref,x))

print(np.min(vals))
print(np.max(vals))

#plot the histogram: change counts and bins to fit your data
plt.hist(vals[:28], alpha=0.75,bins=[.1,.15,.2,.25,.3,.35,.4])
plt.hist(vals[28:56], alpha=0.75,bins=[.1,.15,.2,.25,.3,.35,.4])
plt.hist(vals[56:], alpha=0.75,bins=[.15,.2,.25,.3,.35,.4])
plt.xticks(np.arange(.1, .45, .05))
plt.yticks(np.arange(0, 16, 5))

plt.xlabel('RMSD')
plt.ylabel('Count')
plt.legend(['10A','14A','18A'])
plt.savefig('RMSD_plot.pdf',dpi=300)
