"""
ID: edward.10
LANG: PYTHON3
TASK: milk3
"""

A, B, C = range(3)

def get_capacities():
    with open('milk3.in', 'r') as f:
        capacities = map(int, f.readline().split())
        return tuple(capacities)


def pour(source, dest, buckets, capacities):
    amount = buckets[source]
    capacity = capacities[dest] - buckets[dest]

    amount = min(amount, capacity)

    buckets_ = list(buckets)
    buckets_[source] -= amount
    buckets_[dest] += amount
    return tuple(buckets_)


def expand(buckets):
    neighbors = []
    for source in A, B, C:
        for dest in A, B, C:
            if source == dest:
                continue

            neighbor = pour(source, dest, buckets, capacities)
            neighbors.append(neighbor)

    return neighbors


if __name__ == '__main__':
    capacities = get_capacities()

    frontier = set([(0, 0, capacities[-1])])
    while True:
        frontier_ = set()
        for buckets in frontier:
            neighbors = expand(buckets)
            frontier_.update(neighbors)

        if frontier_ == frontier:
            frontier = frontier_
            break

        frontier = frontier_

    amounts = [c for a, b, c in frontier if a == 0]

    with open('milk3.out', 'w') as f:
        f.write(
            ' '.join(
                map(str, sorted(amounts))
            ) + '\n'
        )

