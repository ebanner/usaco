def copy(A):
    m = len(A[0])
    return [[0]*m for row in A]

def rot90(A):
    A_rot = copy(A)

    n, m = len(A), len(A[0])

    J = range(m-1, -1, -1)
    I = range(n)
    for k in range(n):
        for j, i in zip(J, I):
            A_rot[i][k] = A[k][j]

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

    def swap_col(j):
        for i in range(n):
            A[i][j], A[i][m-1-j] = A[i][m-1-j], A[i][j]

    for j in range(m // 2):
        swap_col(j)

    return A


if __name__ == '__main__':
    A = [['@', '@'], 
        ['-', '-']]

    for row in A:
        print(row)
    print()

    A_rot = rot90(A)

    for row in A_rot:
        print(row)
    print()

    A_rot_rot = rot90(A_rot)

    for row in A_rot_rot:
        print(row)
