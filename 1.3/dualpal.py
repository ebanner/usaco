"""
ID: edward.10
LANG: PYTHON3
TASK: dualpal
"""


def get_input():
    with open('dualpal.in', 'r') as f:
        N, S = map(int, f.readline().strip().split())

    return N, S


def convert(N, b):
    digits = []
    while N:
        digit = N % b
        digits.append(str(digit))
        N //= b

    return ''.join(reversed(digits))


def is_palindrome(N):
    if N == ''.join(reversed(N)):
        return N


if __name__ == '__main__':
    N, S = get_input()

    s = S + 1

    answers = []
    while True:
        if len(answers) == N:
            break

        num_palindromes = 0
        for b in range(2, 10+1):
            s_b = convert(s, b)
            if is_palindrome(s_b):
                num_palindromes += 1

        if num_palindromes >= 2:
            answers.append(s)
        
        s += 1

    with open('dualpal.out', 'w') as f:
        for answer in answers:
            f.write(str(answer) +  '\n')

