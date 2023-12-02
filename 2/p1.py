lines = []
with open('in.txt', 'r+') as f:
    lines = f.readlines()

possible_games = []
for line in lines:
    parts = line.split()
    id = parts[1][:-1]
    game_results = ' '.join(parts[2:])
    cube_sets = game_results.split(';')
    max_colors = {'red': 0, 'green': 0, 'blue': 0}
    for cset in cube_sets:
        for handful in cset.split(', '):
            match handful.split():
                case [n, color]:
                    max_colors[color] = max(max_colors[color], int(n))

    if max_colors['red'] > 12:
        continue
    if max_colors['green'] > 13:
        continue
    if max_colors['blue'] > 14:
        continue

    possible_games.append(int(id))

print(sum(possible_games))
