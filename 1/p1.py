lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

# Extract all the numbers from each line
lines = list(map(lambda l: ''.join(list(filter(lambda c: c.isnumeric(), l))), lines))
# Extract the first and last digit from every line
lines = map(lambda n: int(n[0] + n[-1]), lines)
print(sum(lines))
