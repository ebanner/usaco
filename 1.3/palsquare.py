"""
ID: edward.10
LANG: PYTHON3
TASK: palsquare
"""


TRANSLATE = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'E',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q',
    27: 'R',
    28: 'S',
    29: 'T',
    30: 'U',
    31: 'V',
    32: 'W',
    33: 'X',
    34: 'Y',
    35: 'Z',
}


def get_base():
    with open('palsquare.in', 'r') as f:
        base = int(f.readline().strip())
        return base


def is_palindrome(N):
    if N == ''.join(reversed(N)):
        return N


def convert(num, base):
    digits = []
    while num:
        digit = num % base
        digits.append(TRANSLATE[digit])
        num //= base

    return ''.join(reversed(digits))


def get_squares(base):
    squares = []
    for N in range(1, 300+1):
        squared = N**2
        squared_converted = convert(squared, base)
        squares.append(squared_converted)

    return squares


if __name__ == '__main__':
    base = get_base()

    squares = get_squares(base)

    nums = [convert(N, base) for N in range(1, 300+1)]

    palindromes = [(N, palindrome) for N, square in zip(nums, squares) if (palindrome := is_palindrome(square))]

    with open('palsquare.out', 'w') as f:
        for N, palindrome in palindromes:
            f.write(f'{N} {palindrome}\n')

