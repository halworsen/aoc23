from functools import reduce

lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

powers = []
for line in lines:
    parts = line.split()
    game_results = ' '.join(parts[2:])
    cube_sets = game_results.split(';')
    max_colors = {'red': 0, 'green': 0, 'blue': 0}
    for cset in cube_sets:
        for handful in cset.split(', '):
            match handful.split():
                case [n, color]:
                    max_colors[color] = max(max_colors[color], int(n))

    powers.append(reduce(lambda x, y: x*y, max_colors.values()))

print(sum(powers))
