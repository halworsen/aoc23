from itertools import product

lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

# input parsing zzz
games = [line.split(':')[1] for line in lines]
# split into 2 lists of numbers, one for the winning numbers and one for the hand
games = [[list(map(int, nums.split())) for nums in g.split('|')] for g in games]

# filter out the numbers that appear in both lists
matching_nums = list(map(lambda g: [n[0] for n in product(g[0], g[1]) if n[0] == n[1]], games))

# compute the score based on the amount of elements in each list
score = [(2**(len(m)-1) if len(m) else 0) for m in matching_nums]
print(sum(score))
