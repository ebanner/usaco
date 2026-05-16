"""
ID: edward.10
LANG: PYTHON3
TASK: skidesign
"""

def get_hills():
    with open('skidesign.in', 'r') as f:
        n = int(f.readline())
        lines = [f.readline() for _ in range(n)]
        hills = [int(line) for line in lines]
        return hills


def get_cost(min, max, hills):
    cost = 0
    for hill in hills:
        if min <= hill <= max:
            continue

        if hill < min:
            cost += (min-hill)**2
        elif max < hill:
            cost += (hill-max)**2

    return cost


def get_hill_ranges(hills):
    hill_ranges = []
    for i in range(min(hills), max(hills)):
        hill_range = (i, i+17)
        hill_ranges.append(hill_range)

    return hill_ranges


if __name__ == '__main__':
    hills = get_hills()

    hill_ranges = get_hill_ranges(hills)

    min_cost = float('inf')
    for hill_range in hill_ranges:
        cost = get_cost(*hill_range, hills)
        min_cost = min(cost, min_cost)

    with open('skidesign.out', 'w') as f:
        f.write(str(min_cost) + '\n')
