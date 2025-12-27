"""
ID: edward.10
LANG: PYTHON3
TASK: transform
"""


def zeros(A):
    n = len(A)
    A_zero = [[0]*n for row in A]
    return A_zero


def copy(A):
    A_copy = [row[:] for row in A]
    return A_copy


def get_original():
    with open('transform.in', 'r') as f:
        N = int(f.readline().strip())

        original = []
        for _ in range(N):
            line = f.readline().strip()
            row = list(line)
            original.append(row)

    return original


def get_desired():
    with open('transform.in', 'r') as f:
        N = int(f.readline().strip())

        for _ in range(N):
            f.readline()

        desired = []
        for _ in range(N):
            line = f.readline().strip()
            row = list(line)
            desired.append(row)

    return desired


def rot90(A):
    n = len(A)

    A_rot = zeros(A)
    for k in range(n-1, -1, -1):
        I, J = range(n), range(n)
        for i, j in zip(I, J):
            A_rot[i][k] = A[n-k-1][j]
            A_rot[i][k] = A[n-k-1][j]

    return A_rot


def rot180(A):
    A_rot = rot90(A)
    A_rot_rot = rot90(A_rot)
    return A_rot_rot


def rot270(A):
    A_rot_rot = rot180(A)
    A_rot_rot_rot = rot90(A_rot_rot)
    return A_rot_rot_rot


def reflect(A):
    n, m = len(A), len(A[0])

    A_reflected = copy(A)

    def swap_col(j):
        for i in range(n):
            A_reflected[i][j], A_reflected[i][m-1-j] = A_reflected[i][m-1-j], A_reflected[i][j]

    for j in range(m // 2):
        swap_col(j)

    return A_reflected


if __name__ == '__main__':
    original = get_original()
    desired = get_desired()

    transforms = [
        (rot90, 1),
        (rot180, 2), 
        (rot270, 3), 
        (reflect, 4),
        (lambda grid: rot90(reflect(grid)), 5),
        (lambda grid: rot180(reflect(grid)), 5),
        (lambda grid: rot270(reflect(grid)), 5),
        (lambda x: x, 6)
    ]

    transformation_idx = None
    for transform, idx in transforms:
        transformed = transform(original)

        if transformed == desired:
            transformation_idx = idx
            break
    else:
        transformation_idx = 7
    
    with open('transform.out', 'w') as f:
        f.write(str(transformation_idx) + '\n')
