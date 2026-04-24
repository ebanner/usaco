"""
ID: edward.10
LANG: PYTHON3
TASK: barn1
"""

def get_input():
    with open('barn1.in', 'r') as f:
        M, S, C = f.readline().strip().split()

    return map(int, [M, S, C])


def get_cows(C):
    with open('barn1.in', 'r') as f:
        f.readline().strip().split()

        cows = []
        for _ in range(C):
            cow = int(f.readline().strip())
            cows.append(cow)

    return cows


def get_gaps(cows):
    gaps = [((c2-c1), i) for i, (c1, c2) in enumerate(zip(cows, cows[1:]))]
    return gaps


if __name__ == '__main__':
    M, S, C = get_input()
    cows = sorted(get_cows(C))
    gaps = get_gaps(cows)

    if M > 1:
        largest_gaps = sorted(gaps, reverse=True)[:M-1]
        largest_gap_idxs = sorted(i for (_, i) in largest_gaps)

        boards = \
            [([0, largest_gap_idxs[0]])] + \
            [[i+1, j] for i, j in list(zip(largest_gap_idxs, largest_gap_idxs[1:]))] + \
            [[largest_gap_idxs[-1]+1, C-1]]
    else:
        board = [0, C-1]
        boards = [board]

    num_stalls_blocked = sum(cows[j]-cows[i]+1 for i, j in boards)

    with open('barn1.out', 'w') as f:
        f.write(str(num_stalls_blocked) + '\n')

