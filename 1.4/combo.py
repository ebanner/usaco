"""
ID: edward.10
LANG: PYTHON3
TASK: combo
"""


def get_dial_size():
    with open('combo.in', 'r') as f:
        dial_size = int(f.readline().strip())
    return dial_size


def get_passcodes():
    with open('combo.in', 'r') as f:
        f.readline()
        fj_passcode = map(int, f.readline().strip().split())
        master_passcode = map(int, f.readline().strip().split())
    return tuple(fj_passcode), tuple(master_passcode)


DELTAS = (-2, -1, 0, 1, 2)

def get_combos(combo, dial_size):
    combo = map(lambda x: x-1, combo)
    combo = tuple(combo)

    combos = set()
    for di in DELTAS:
        for dj in DELTAS:
            for dk in DELTAS:
                combo_ = (x+y for x, y in zip((di, dj, dk), combo))
                combo_ = map(lambda x: x%dial_size, combo_)
                combo_ = map(lambda x: x+1, combo_)
                combo_ = tuple(combo_)
                combos.add(combo_)

    return combos


if __name__ == '__main__':
    dial_size = get_dial_size()
    fj_passcode, master_passcode = get_passcodes()

    combos = \
        get_combos(fj_passcode, dial_size) | \
        get_combos(master_passcode, dial_size)

    num_combos = len(combos)

    with open('combo.out', 'w') as f:
        f.write(str(num_combos) + '\n')
