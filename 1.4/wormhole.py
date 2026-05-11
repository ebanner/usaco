"""
ID: edward.10
LANG: PYTHON3
TASK: wormhole
"""

def parse(line):
    x, y = map(int, line.split())
    return x, y


def get_wormholes():
    with open('wormhole.in', 'r') as f:
        n = int(f.readline())
        lines = [f.readline() for _ in range(n)]
        wormholes = {parse(line) for line in lines}
        return wormholes


def without(lst, val):
     return [elem for elem in lst if elem != val]


def get_pairings(wormholes):
    pairings = []
    def get_pairings_(pairs, remaining):
        if remaining == []:
            pairings.append(pairs)
            return

        first, *rest = remaining
        for wormhole in rest:
            pair = (first, wormhole)
            get_pairings_(
                pairs + [pair], 
                without(rest, wormhole)
            )

    get_pairings_([], wormholes)

    return frozenset(
        frozenset(pairing) for pairing in pairings
    )


def get_dict(pairing):
    wormhole_dict = {}
    for a, b in pairing:
        wormhole_dict[a] = b
        wormhole_dict[b] = a

    return wormhole_dict


def sub(x1, y1, x2, y2):
    return ((x1-x2), (y1-y2))


def add(x1, y1, x2, y2):
    return ((x1+x2), (y1+y2))


def get(x, y, wormholes):
    candidates = []
    for x_, y_ in wormholes:
        if y_ == y and x_ > x:
            candidate = (x_, y_)
            candidates.append(candidate)

    if not candidates:
        return None

    return min(candidates, key=lambda wormhole: wormhole[0])


epsilon = 0.1

def has_cycle(pairing, wormholes):
    """

    pairing = next(iter(pairings))

    """
    wormhole_dict = get_dict(pairing)

    def has_cycle_(pos, path=[]):
        wormhole = get(*pos, wormholes)
        if not wormhole:
            return False

        if wormhole in path:
            return True

        path_ = path + [wormhole]
        pos_ = add(*wormhole_dict[wormhole], *(epsilon,0))
        return has_cycle_(pos_, path_)

    for wormhole in wormholes:
        start = sub(*wormhole, *(epsilon, 0))
        if has_cycle_(start):
            return True

    return False


if __name__ == '__main__':
    wormholes = get_wormholes()

    pairings = get_pairings(wormholes)

    num_cycles = 0
    for pairing in pairings:
        if has_cycle(pairing, wormholes):
            num_cycles += 1

    with open('wormhole.out', 'w') as f:
        f.write(str(num_cycles) + '\n')

