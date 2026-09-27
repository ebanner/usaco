"""
ID: edward.10
LANG: PYTHON3
TASK: numtri
"""

def get_triangle():
    with open('numtri.in', 'r') as f:
        R = int(f.readline())
        rows = []
        for _ in range(R):
            row = map(int, f.readline().split())
            rows.append(list(row))

    def pad(row, level):
        zeros = [0]*(R-level-1)
        padded = zeros + row + zeros
        return padded

    rows_ = []
    for row in rows:
        row_ = interleave(row)
        rows_.append(row_)

    triangle = []
    for i, row in enumerate(rows_):
        row_ = pad(row, i)
        triangle.append(row_)

    return triangle


def interleave(row):
    return eval('[' + ', 0, '.join(map(str, row)) + ']')


def get_init(triangle):
    R = len(triangle)
    init = [[0]*(2*R-1) for _ in range(R)]
    init[0][R-1] = triangle[0][R-1]
    return init


if __name__ == '__main__':
    triangle = get_triangle()

    dp = get_init(triangle)

    R = len(triangle)

    for i in range(R-1):
        for j in range(1, 2*R-2):
            dp[i+1][j-1] = max(
                dp[i][j] + triangle[i+1][j-1],
                dp[i+1][j-1]
            )

            dp[i+1][j+1] = max(
                dp[i][j] + triangle[i+1][j+1],
                dp[i+1][j+1]
            )

    result = max(dp[R-1])

    with open('numtri.out', 'w') as f:
        f.write(str(result) + '\n')
