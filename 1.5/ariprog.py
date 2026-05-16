"""
ID: edward.10
LANG: PYTHON3
TASK: ariprog
"""

def get_input():
    with open('ariprog.in', 'r') as f:
        N = int(f.readline())
        M = int(f.readline())
        return N, M


def get_bisquares(M):
    bisquares = set()
    for i in range(M+1):
        for j in range(M+1):
            bisquare = i**2 + j**2
            bisquares.add(bisquare)

    return bisquares


def get_sorted(sequences):
    sorted_sequences = sorted(
        sequences,
        key=lambda x: (x[1], x[0])
    )

    return sorted_sequences


def serialize(sequence):
    """

    sequence, *_ = sequences

    """
    return ' '.join(map(str, sequence))


if __name__ == '__main__':
    N, M = get_input()

    S = get_bisquares(M)

    def test(a, b):
        for i in range(N):
            term = a + i*b
            if term not in S:
                return False
        return True

    B = max(S)

    sequences = []
    for a in S:
        for b in range(1, 2*M**2):
            if a + (N-1)*b > B:
                break

            if test(a, b):
                sequence = (a, b)
                sequences.append(sequence)

    with open('ariprog.out', 'w') as f:
        if not sequences:
            f.write("NONE" + '\n')
        else:
            sorted_sequences = get_sorted(sequences)
            for sequence in sorted_sequences:
                f.write(serialize(sequence) + '\n')
