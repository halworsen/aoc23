import re

lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pat = re.compile(f'(?=({"|".join(digits)}))')

# Sub in the number at each digit word in each line
# Basically just find all instances of digits as words, then put the corresponding number in front
lines = map(lambda l: pat.sub(lambda m: str(digits.index(m.group(1))+1), l), lines)
# Extract all the numbers from each line
lines = map(lambda l: ''.join(list(filter(lambda c: c.isnumeric(), l))), lines)
# Extract the first and last digit from every line
lines = list(map(lambda n: int(n[0] + n[-1]), lines))
print(sum(lines))
