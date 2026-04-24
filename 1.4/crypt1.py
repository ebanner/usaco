"""
ID: edward.10
LANG: PYTHON3
TASK: crypt1
"""


def get_digits():
    with open('crypt1.in', 'r') as f:
        N = f.readline()
        digits = map(int, f.readline().strip().split())

    return set(digits)


if __name__ == '__main__':
    DIGITS = get_digits()

    def test(x1, x2, x3, x4, x5):
        """
           x5 x4 x3 = X1
           *  x2 x1 = X2
        -----------
        +  y3 y2 y1 = Y1
        y6 y5 y4    = Y2
        -----------
                  Y
        """
        def combine(*xs):
            return int(''.join(map(str, xs)))

        def length(Y):
            return len(str(Y))

        def digits(Y):
            return {int(d) for d in str(Y)}

        X1 = combine(x5, x4, x3)
        Y1 = X1 * x1
        Y2 = X1 * x2

        if length(Y1) != 3 or not digits(Y1) <= DIGITS:
            return False

        if length(Y2) != 3 or not digits(Y2) <= DIGITS:
            return False

        Y = Y1 + Y2*10

        if length(Y) != 4 or not digits(Y) <= DIGITS:
            return False

        return True

    def get_solutions(solution=[]):
        if len(solution) == 5:
            return [solution] if test(*solution) else []

        solutions = []
        for digit in DIGITS:
            solutions_ = get_solutions(solution+[digit])
            solutions.extend(solutions_)
            
        return solutions

    solutions = get_solutions()

    with open('crypt1.out', 'w') as f:
        f.write(str(len(solutions)) + '\n')

