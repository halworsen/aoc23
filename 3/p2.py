import re
import numpy as np
import itertools
np.set_printoptions(linewidth=np.inf)

lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

n_pat = re.compile(r'(\d+)')
symbols = '*'

# first pass to turn the input into a filter matrix where symbols = 1 and everything else = 0
sym_matrix = np.zeros((len(lines), len(lines[0])), dtype=np.uint32)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        sym_matrix[i, j] = (1 if c in symbols else 0)
# pad the matrix
sym_matrix = np.pad(sym_matrix, 1, constant_values=0)
part_matrix = sym_matrix.copy()
ratio_matrix = sym_matrix.copy()

# second pass to filter numbers that have adjacent symbols
parts = []
for n, line in enumerate(lines):
    for m in n_pat.finditer(line):
        part_number = int(m.group(1))
        start = m.start()
        width = (m.end() - start) + 2

        # grab the surrounding region as a filter from the symbol matrix
        num_matrix = np.full((3, width), part_number)
        filter = sym_matrix[n:n+3, start:start+width]

        part_matrix[n:n+3, start:start+width] = num_matrix * filter
        ratio_matrix[n:n+3, start:start+width] = num_matrix * ratio_matrix[n:n+3, start:start+width]

# weed out the part numbers that didn't get multiplied into a gear ratio
ratios = np.where(ratio_matrix != part_matrix, ratio_matrix, 0)

print(ratios.sum())
