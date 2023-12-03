import re
import numpy as np

lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

n_pat = re.compile(r'(\d+)')
symbols = '*#+-$/&%=@'

# first pass to turn the input into a filter matrix where symbols = 1 and everything else = 0
sym_matrix = np.zeros((len(lines), len(lines[0])), dtype=np.uint8)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        sym_matrix[i, j] = (1 if c in symbols else 0)
# pad the matrix
sym_matrix = np.pad(sym_matrix, 1, constant_values=0)

# second pass to filter numbers that have adjacent symbols
part_sum = 0
for n, line in enumerate(lines):
    for m in n_pat.finditer(line):
        part_number = int(m.group(1))
        start = m.start()
        width = (m.end() - start) + 2

        # grab the surrounding region as a filter from the symbol matrix
        num_matrix = np.full((3, width), part_number, dtype=np.uint16)
        filter = sym_matrix[n:n+3, start:start+width]

        # multiply them together to extract the number only if there was an adjacent symbol
        filtered = num_matrix * filter
        part_sum += filtered.sum()

print(part_sum)
