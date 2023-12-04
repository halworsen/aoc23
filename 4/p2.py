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

# find out how many copies we get of the following scratchcards
copies = list(map(len, matching_nums))

# then start counting the amount of scratchcards
num_cards = [1] * len(copies)
for n, num_copies in enumerate(copies):
    for i in range(num_copies):
        num_cards[n + i + 1] += num_cards[n]

print(sum(num_cards))
