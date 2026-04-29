"""
ID: edward.10
LANG: PYTHON3
TASK: combo
"""


def get_dial_size():
    with open('combo.in', 'r') as f:
        dial_size = int(f.readline().strip())
    return dial_size


def get_combinations():
    with open('combo.in', 'r') as f:
        f.readline()
        fj_passcode = map(int, f.readline().strip().split())
        master_passcode = map(int, f.readline().strip().split())
    return list(fj_passcode), list(master_passcode)


def opens(c1, c2, N):
    def dist(i, j):
        d = abs(i-j)
        return min(d, N-d)

    for i, j in zip(c1, c2):
        if not dist(i, j) <= 2:
            return False

    return True


if __name__ == '__main__':
    dial_size = get_dial_size()
    fj_passcode, master_passcode = get_combinations()

    num_settings = 0
    for i in range(1, dial_size+1):
        for j in range(1, dial_size+1):
            for k in range(1, dial_size+1):
                combo = (i, j, k)
                if opens(combo, fj_passcode, dial_size) and opens(combo, master_passcode, dial_size):
                    num_settings += 1
                elif opens(combo, fj_passcode, dial_size):
                    num_settings += 1
                elif opens(combo, master_passcode, dial_size):
                    num_settings += 1

    with open('combo.out', 'w') as f:
        f.write(str(num_settings) + '\n')
